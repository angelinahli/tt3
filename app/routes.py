"""
filename: routes.py
author: Angelina Li, Kate Kenneally, Priscilla Lee
last modified: 05/24/2018
description: routes for app
"""

from datetime import datetime
from flask import render_template, flash, request, redirect, url_for, \
    session, jsonify

from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index/")
def index():
    params = {}
    return render_template("index.html", **params)

@app.route("/login/")
def login():
    params = {"title": "Login"}
    form = LoginForm()
    params["form"] = form
    return render_template("login_mdl.html", **params)
