#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12/0012 23:04
# @Author  : Mat
import random

from flask import Blueprint, render_template, request, g, current_app, redirect, url_for, flash
from flask.json import jsonify
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db, cache
from App.models import News, Student
from App.utils import send_code

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return 'index'


@blue.route('/addnews/')
def add_news():
    news = News()
    news.n_title = '周润发%d' % random.randrange(10000)
    news.n_content = '福利社会%d' % random.randrange(10000)

    db.session.add(news)
    db.session.commit()

    return 'add success'


@blue.route('/getnews/')
def get_news():
    news = News.query.all()
    new_content = render_template('new_content.html', news=news)
    print(new_content)
    return render_template('news.html', new_content=new_content)


@blue.before_request
def before():
    g.msg = '哈哈哈'  # 全局参数
    conf = current_app.config
    print(request.url)
    print(conf)


@blue.after_request
def after(response):
    print('after')
    print(response)
    print(type(response))

    return response


@blue.route('/student/register/', methods=['GET', "POST"])
def student_register():
    if request.method == 'GET':
        return render_template('StudentRegister.html')

    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')

        # hash_psd = generate_password_hash(password)
        # hash_psd = password
        code = request.form.get('code')
        cache_code = cache.get(username)
        print("验证码", code,cache_code)
        if code != cache_code:
            return '验证失败'

        student = Student()
        student.s_name = username
        student.s_password = password  # model 里面已经做了处理了
        student.s_phone = phone
        db.session.add(student)
        db.session.commit()

        return '注册成功'


@blue.route('/student/login/', methods=['GET', "POST"])
def student_login():
    if request.method == 'GET':
        return render_template('StudentLogin.html')

    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # 先要去查数据库
        stu = Student.query.filter(Student.s_name.__eq__(username)).first()
        if stu and stu.check_password(password):
            return 'login success'
        flash('用户名或密码错误') # 向前端页面传输数据
        return redirect(url_for('blue.student_login'))

#
# @blue.route('/sendmail/')
# def send_mail():
#     msg = Message('flask email', recipients=['',])
#     msg.body = '哈哈哈哈哈哈'
#     msg.html = '<h1>this is  a  good </h1>'
#     mail.send(message=msg)
#
#     return '邮件发送成功'


@blue.route('/sendcode/')
def send_code1():
    phone = request.args.get('phone')
    username = request.args.get('username')
    print('send_code username: ', username, phone)
    respo = send_code(phone)
    result = respo.json()
    if result.get('code') == 200:
        obj = result.get('obj')
        print('obj', obj)
        cache.set(username, obj)
        data = {
            'msg': "ok",
            'status': 200
        }
        return jsonify(data)
    # print(respo.json())
    data = {
        'msg': 'fail',
        'status': 400
    }
    return jsonify(data)