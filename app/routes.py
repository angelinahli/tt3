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
from app.forms import LoginForm, SignUpForm

@app.route("/")
@app.route("/index/")
def index():
    params = {}
    is_logged_in = lambda: False

    if not is_logged_in(): # implement this
        login_form = LoginForm()
        sign_up_form = SignUpForm()
        params["login_form"] = login_form
        params["sign_up_form"] = sign_up_form

    else:
        u = current_user # implement this
    return render_template("index.html", **params)
