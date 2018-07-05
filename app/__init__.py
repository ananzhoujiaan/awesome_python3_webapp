#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 12:11
# @Author  : anan
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.debug=True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////pycharm/awesome_python3_webapp/app/test.db' #当前目录下的data.sqlite
db=SQLAlchemy(app)

from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)