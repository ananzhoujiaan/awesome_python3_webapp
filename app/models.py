#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 12:12
# @Author  : anan
# @Site    : 
# @File    : models.py
# @Software: PyCharm

from datetime import datetime
from app import db


class Userlog(db.Model):
    __tablename__ = "userlog"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    # （下面是设置外键的第一步）:指向user表的id字段
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # ip地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return '<User %r>' % self.id
