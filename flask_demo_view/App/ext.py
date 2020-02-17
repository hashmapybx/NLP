#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 1:31
# @Author  : Mat

# 该文件是用来管理第三方的插件的
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
models = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    '''
    专门用于初始化扩展库文件 初始化第三方的库文件
    :param app:
    :return:
    '''
    models.init_app(app=app)
    migrate.init_app(app, models) # 初始化
