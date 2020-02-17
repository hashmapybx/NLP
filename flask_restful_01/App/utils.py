#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13/0013 19:16
# @Author  : Mat
import hashlib
import time

import requests


def send_code(phone):
    url = 'https://api.netease.im/sms/sendcode.action'
    nonce = hashlib.new('sha512', str(time.time()).encode('utf-8')).hexdigest()

    curtime = str(int(time.time()))

    sha1 = hashlib.sha1()
    secret = "bd025fa9e32c"

    sha1.update((secret+nonce + curtime).encode('utf-8'))

    check_sum = sha1.hexdigest()

    header = {
        "AppKey": "14135a048a60661011bc249885d62507",
        "Nonce": nonce,
        "CurTime":curtime,
        "CheckSUm": check_sum,
    }

    post_data = {
        "mobile": phone

    }

    response = requests.post(url, data=post_data, headers=header)
    # print(response.content)
    return response