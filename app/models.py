#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from app import db, login

class User(db.Model, UserMixin):
    pass
