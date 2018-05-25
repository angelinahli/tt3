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
    login_form = LoginForm()
    sign_up_form = SignUpForm()
    params["login_form"] = login_form
    params["sign_up_form"] = sign_up_form
    return render_template("index.html", **params)

@app.route("/login/")
def login():
    params = {"title": "Login", "notitle": True}
    form = LoginForm()
    params["form"] = form
    return render_template("login.html", **params)

@app.route("/signup/")
def sign_up():
    params = {"title": "Sign Up", "notitle": True}
    form = SignUpForm()
    params["form"] = form
    return render_template("sign_up.html", **params)
