#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
filename: app.py
authors: Angelina Li,
last modified: 05/21/2018
description: initializes application
"""

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
login = LoginManager(app)
login.login_view = "login"

from app import routes
