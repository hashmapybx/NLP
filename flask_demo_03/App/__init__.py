#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:04
# @Author  : Mat
from flask import Flask

from App.ext import init_ext
from App.middleware import load_middle
from App.settings import envs
from App.views import init_blue

def create_app(env):

    app = Flask(__name__)

    app.config.from_object(envs.get(env))

    init_ext(app)

    init_blue(app)
    # load_middle(app) # 加载中间件
    return app