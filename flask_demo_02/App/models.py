#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 0:05
# @Author  : Mat


from App.ext import models

class User(models.Model):
    __tablename__ = 'user'
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(20))

    def __repr__(self):
        return "<User %r>" % self.username
