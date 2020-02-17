#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:37
# @Author  : Mat
from flask import Blueprint

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Index'

# # 添加参数
# @blue.route('/rule/<id>/')
# def get_id(id):
#     print(id)
#     print(type(id))
#     return 'sucess'

# 获取参数 设置类型
@blue.route('/user/<int:id>/')
def get_user(id):
    print(id)
    print(type(id))
    return 'user.id{%d}' % id

# 可以添加多个路由实现代码复用操作

@blue.route('/info/<string:name>/')
@blue.route('/getinfo/<int:name>/')
def get_name(name):
    print(name)
    print(type(name))
    return 'get Sucess name'


@blue.route('/add/<path:address>/')
def get_address(address):
    print(address)
    print(type(address))
    return 'get Sucess adress'

@blue.route('/getuuid/<uuid:number>/')
def get_uuid(number):
    print(number)
    print(type(number))
    return 'get Sucess uuid'

@blue.route('/getany/<any(a, b):an>/') # an 的值只能是a 或者 b
def get_any(an):
    print(an)
    print(type(an))
    return 'get Sucess an'