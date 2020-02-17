#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:04
# @Author  : Mat
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 加载配置信息

    app.config.from_object(envs.get(env))
    # 初始化第三方库
    init_ext(app)
    # 初始化路由
    init_blue(app)
    return app
