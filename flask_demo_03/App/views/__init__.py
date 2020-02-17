#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:37
# @Author  : Mat
from App.views.Helloblue import blue


def init_blue(app):
    app.register_blueprint(blue)
