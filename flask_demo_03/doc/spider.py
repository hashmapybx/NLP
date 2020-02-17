#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/12/0012 23:24
# @Author  : Mat

import requests

def get_data():
    path = 'http://127.0.0.1:5000/getnews/'
    response = requests.get(path)
    print(response.content.decode('utf8'))

if __name__ == '__main__':
    get_data()