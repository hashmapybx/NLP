#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:38
# @Author  : Mat
from flask import Blueprint
second = Blueprint('second', import_name=__name__)
# 也是可以有多个蓝图的



@second.route('/hello/')
def hello():
    return "this is hello"
