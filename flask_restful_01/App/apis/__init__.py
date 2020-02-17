#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14/0014 10:54
# @Author  : Mat

from flask_restful import Api
from App.apis.HelloApi import HelloResource
from App.apis.goods_api import GoodsListResource

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(HelloResource, '/hello/') # 第二参数表示的是路由

api.add_resource(GoodsListResource, '/goods/')