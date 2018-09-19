#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
filename: app.py
authors: Angelina Li,
last modified: 05/21/2018
description: initializes application
"""

from configurations import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = "login"

from app import routes, models
