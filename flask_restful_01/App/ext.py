#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 1:31
# @Author  : Mat

# 该文件是用来管理第三方的插件的
from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
# mail = Mail()
cache = Cache(
    config= {
        "CACHE_TYPE": 'redis',
    }
)
def init_ext(app):
    '''
    专门用于初始化扩展库文件 初始化第三方的库文件
    :param app:
    :return:
    '''
    db.init_app(app=app)
    migrate.init_app(app, db) # 初始化
    # mail.init_app(app)
    cache.init_app(app)