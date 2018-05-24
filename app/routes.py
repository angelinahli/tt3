"""
filename: routes.py
author: Angelina Li, Kate Kenneally, Priscilla Lee
last modified: 05/24/2018
description: routes for app
"""

from app import app
from datetime import datetime
from flask import render_template, flash, request, redirect, url_for, \
    session, jsonify

@app.route("/")
@app.route("/index/")
def index():
    return "Hello!"
