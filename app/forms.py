#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import wtforms as wtf
import datetime as dt
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError

class LoginForm(FlaskForm):    
    email = wtf.StringField(
        "Enter your Wellesley email", 
        validators=[DataRequired()])
    password = wtf.PasswordField("Password", validators=[DataRequired()])
    remember_me = wtf.BooleanField("Remember Me")
    submit = wtf.SubmitField("Login")

class SignUpForm(FlaskForm):
    name = wtf.StringField(
        "Enter your name",
        validators=[DataRequired()])
    email = wtf.StringField(
        "Enter your Wellesley email",
        validators=[DataRequired()])
    password = wtf.PasswordField("Password", validators=[DataRequired()])
    submit = wtf.SubmitField("Sign up")

class NewSessionForm(FlaskForm):
    username = wtf.StringField(
        "Enter your Wellesley username", 
        validators=[DataRequired()])
