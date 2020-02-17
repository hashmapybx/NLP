#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14/0014 10:54
# @Author  : Mat
from flask_restful import Resource


class HelloResource(Resource):
    def get(self):
        return {'msg': 'ok'}
