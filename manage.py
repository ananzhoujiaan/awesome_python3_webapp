#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 12:10
# @Author  : anan
# @Site    : 
# @File    : manage.py.py
# @Software: PyCharm

from app import app

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5002)

