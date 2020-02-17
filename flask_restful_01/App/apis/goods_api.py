#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14/0014 13:38
# @Author  : Mat
from flask import request
from flask_restful import Resource, abort, fields, marshal, marshal_with

from App.models import Goods

goods_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='g_name'),
    'g_price':fields.Float,
}

# 多字段 或者是少字段是没有影响的 对于返回的对象
single_goods_fields = {
    "data": fields.Nested(goods_fields),
    'msg': fields.String,
    'status': fields.Integer,
    'hahaha': fields.String,
    'hadoop':fields.String
}

multi_goods_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(goods_fields)), # 级联的嵌套
}

'''
上面good_fields single _fields multi_goods_fields 其实就是用来定义了你想要返回的数据对象的格式

'''

class GoodsListResource(Resource):

    @marshal_with(multi_goods_fields)
    def get(self):

        goods_list = Goods.query.all()
        data = {
            "msg": "ok",
            "status": 200,
            "data": goods_list,
        }
        return data
    @marshal_with(single_goods_fields)
    def post(self):
        g_name = request.form.get('g_name')
        g_price = request.form.get('g_price')
        goods = Goods()
        goods.g_name = g_name
        goods.g_price = g_price
        if not goods.save():
            abort(400)
        else:
            data = {
                "msg": "create success",
                'status': 201,
                # 需要对goods对象进行序列化
                # 'data': marshal(goods, goods_fields),
                'data': goods, # 这种方式怎么解决呢 看官方文档
            }
            return  data
