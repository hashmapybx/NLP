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
    # 数据库的url 数据库+驱动://用户名:密码@主机:端口/具体那一个库
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_demo'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(envs.get(env))
    # 通过懒加载的训练导入 通过参数把app传入 调用视图函数
    # init_router(app)
    # app.register_blueprint(blueprint=blue)
    # app.register_blueprint(second)
    # 上面的注册代码太多了 直接注册views文件夹
    # init_model(app)

    init_ext(app)
    init_blue(app)
    return app