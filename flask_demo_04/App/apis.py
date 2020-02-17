#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13/0013 21:49
# @Author  : Mat
from flask_restful import Api, Resource

api = Api()

def init_api(app):
    api.init_app(app)



class HelloResource(Resource):
    def get(self):

        return {'msg':'hello api'}

api.add_resource(HelloResource, '/')