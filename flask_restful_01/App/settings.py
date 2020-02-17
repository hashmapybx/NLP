#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 1:31
# @Author  : Mat
import os

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #文件夹的根目录

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'hadoopandhive'

def get_url(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    username = dbinfo.get("USERNAME") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, username, password, host, port, name)


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USERNAME": "root",
        "PASSWORD": "root",
        "HOST": 'localhost',
        "PORT": "3306",
        "NAME": "flask_restful_01",

    }

    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)
    # MAIL_SERVER = 'smtp.163.com'
    #     # MAIL_PORT = 25
    #     # MAIL_USERNAME = '' # 自己的邮箱地址
    #     # MAIL_PASSWORD = '' # 授权码
    #     # MAIL_DEFAULT_SENDER = MAIL_USERNAME

class TestingConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USERNAME": "root",
        "PASSWORD": "root",
        "HOST": 'localhost',
        "PORT": "3306",
        "NAME": "flask_model_03",

    }

    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)

# 演示环境
class StagingConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USERNAME": "root",
        "PASSWORD": "root",
        "HOST": 'localhost',
        "PORT": "3306",
        "NAME": "flask_model_03",

    }
    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)


class ProductionConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USERNAME": "root",
        "PASSWORD": "root",
        "HOST": 'localhost',
        "PORT": "3306",
        "NAME": "flask_demo",

    }
    SQLALCHEMY_DATABASE_URI = get_url(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
    "default": DevelopConfig,
}