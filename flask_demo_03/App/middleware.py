#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13/0013 9:32
# @Author  : Mat
from flask import request


def load_middle(app):

    @app.before_request
    def before():
        pass
        # print('中间件', request.url)

        '''
        可以实现的功能是优先级
        统计
        反爬
        频率
        用户认证
        权限
        
        '''
    # @app.after_request
    # def after(response):
    #
    #
    #     return response