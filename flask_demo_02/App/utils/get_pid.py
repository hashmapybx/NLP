#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 17:01
# @Author  : Mat

'''
从检查报告中获取到病人的id
PATIENT_ID	PATIENT_LOCAL_ID

'''
import pandas as pd
import os
path = r'D:\PycharmProjects\flask_demo_02\App\utils\2020-01-26_18_56.csv'

df = pd.read_csv(path, encoding='gbk')
# pid = set(list(df['PATIENT_LOCAL_ID'].values))
dict_ = df.set_index('PATIENT_LOCAL_ID').to_dict(orient='index')

# print(dict_.__getitem__(31906137657))




nn = set()
with open(r'D:\PycharmProjects\flask_demo_02\App\utils\阴阳性_pid.txt', 'r') as fin:
    for line in fin.readlines():
        line = line.replace('\n', '').strip()
        nn.add(line)



list_dict = []
for s in nn:
    if int(s) in dict_.keys():
        # print(dict_.get(s, None))
        list_dict.append(dict_.__getitem__(int(s)))

df_1 = pd.DataFrame(data=list_dict[0], index=[0])
for index in range(1, len(list_dict)):

    df_1 = pd.concat([df_1, pd.DataFrame(data=list_dict[index], index=[0])], axis=0)


df.to_csv(r'D:\PycharmProjects\flask_demo_02\App\utils\阴阳性.csv', index=False)





