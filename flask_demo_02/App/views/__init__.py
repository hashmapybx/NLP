#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:37
# @Author  : Mat

from .first_blue import blue
from .second_blue import second


def init_blue(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(second)
