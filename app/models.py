#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO:
    * Implement user-section m:m relations: sections_tutored, sections_taken
      & sections_taught
    * Implement user-tutor m:m visit relation
        * scheduled visits can be recorded as visits with a few added
          attributes
    * Implement tutor-type m:m type relation
        * Are there any type attributes we should note?
"""

from bcrypt import hashpw, checkpw, gensalt
from datetime import datetime
from flask_login import UserMixin

from app import db, login

user_sections_taken = db.Table("user_sections_taken", 
    db.Column("pid", db.Integer, db.ForeignKey("user.pid")),
    db.Column("sid", db.Integer, db.ForeignKey("section.sid"))
)

user_sections_taught = db.Table("user_sections_taught",
    db.Column("pid", db.Integer, db.ForeignKey("user.pid")),
    db.Column("sid", db.Integer, db.ForeignKey("section.sid"))
)

class User(db.Model, UserMixin):
    __tablename__ = "user"
    __table_args__ = {"mysql_engine": "InnoDB"}
    log_rounds = 12

    pid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    full_name = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(512))
    user_type = db.Column(db.String(64), index=True)
    year = db.Column(db.Integer, index=True)

    sections_taken = db.relationship("Section", secondary=user_sections_taken)
    sections_taught = db.relationship("Section", secondary=user_sections_taught)

    def set_password(self, password):
        # password must be a byte object
        self.password_hash = hashpw(password, gensalt())

    def check_password(self, password):
        return checkpw(password, self.password_hash)

    def __repr__(self):
        return "<User #{id}: {username}>".format(**self.__dict__)

class Department(db.Model):
    __tablename__ = "department"
    __table_args__ = {"mysql_engine": "InnoDB"}

    did = db.Column(db.String(5), primary_key=True)
    dept_name = db.Column(db.String(64), index=True, unique=True)
    # perhaps figure out what the lazy attr refers to
    courses = db.relationship("Course", backref="department", lazy="dynamic")

class Course(db.Model):
    __tablename__ = "course"
    __table_args__ = {"mysql_engine": "InnoDB"}

    # should enforce that course code and did should be unique together
    cid = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.Integer, index=True)
    # technically doesn't *need* to be unique.. although that would be better
    course_name = db.Column(db.String(512), index=True)

    # figure out right onupdate value here
    # allow multiple department values!
    did = db.Column(db.Integer, db.ForeignKey("department.id"),
        onupdate="cascade", index=True)
    sections = db.relationship("Section", backref="course", lazy="dynamic")

class SemesterModel:
    # Uncertain what the complete set of semesters looks like
    semester_codes = {
        "winter"    : 1,
        "spring"    : 2,
        "summer"    : 3,
        "summer i"  : 4,
        "summer ii" : 5,
        "fall"      : 6,
        "spring i"  : 7,
        "spring ii" : 8,
        "fall i"    : 9,
        "fall ii"   : 10}
    year = db.Column(db.Integer, index=True)
    semester = db.Column(db.Integer, index=True)

    def set_semester(self, s_name):
        s_name = s_name.lower()
        if s_name not in self.semester_codes:
            raise ValueError("The semester name provided is invalid!")
        self.semester = self.semester_codes.get(s_name)

    def get_semester(self):
        for k, v in self.semester_codes:
            if v == self.semester:
                return k
        msg = "This semester_code - {v} - was set incorrectly.".format(
            v=self.semester)
        raise Exception(msg)

class Section(db.Model, SemesterModel):
    # implement taught_by, taken_by, tutored_by relations
    __tablename__ = "section"
    __table_args__ = {"mysql_engine": "InnoDB"}

    sid = db.Column(db.Integer, primary_key=True)
    section_code = db.Column(db.Integer, index=True)
    cid = db.Column(db.Integer, db.ForeignKey("course.id"), 
        onupdate="cascade", index=True)

class Tutor:
    __tablename__ = "tutor"
    __table_args__ = {"mysql_engine": "InnoDB"}

    uid = db.Column(db.Integer, db.ForeignKey("user.id"))

class VisitType:
    # visit types probably give you information about whether the tutor is
    # attached to 
    __tablename__ = "visit_type"
    __table_args__ = {"mysql_engine": "InnoDB"}
