#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:38
# @Author  : Mat
from flask import Blueprint, render_template
from App.models import models, User
blue = Blueprint(name="blue",import_name=__name__)
# views 里面导入了models

@blue.route('/')
def index():
    # return '我是蓝图的主页' 传参数是和django里面的不一样的
    return render_template('index.html', msg='我饿了')



@blue.route('/createdb/')
def createdb():
    models.create_all()
    return '创建成功'


# 添加数据
@blue.route('/adduser/')
def addUser():

    user = User()
    user.username = 'tom'
    models.session.add(user)
    models.session.commit()
    return '添加成功'


# 删除数据
@blue.route("/dropdb/")
def dropdb():
    models.drop_all()

    return  '删除成功'