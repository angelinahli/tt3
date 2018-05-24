#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", "very-secret-key-123")
