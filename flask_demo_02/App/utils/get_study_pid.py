#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10/0010 17:11
# @Author  : Mat
import os
import pydicom
path_1='/media/tx-eva-data/DR/数据库/标注数据库/test'
fout = open('/media/tx-eva-data/DR/数据库/标注数据库/test/pid.txt', 'wb')
for dirpath, dirname, filenames in os.walk(path_1):
    for filename in filenames:
        dcm_path = os.path.join(dirpath,filename)
        if dcm_path.endswith('.dcm'):
            dcm_folder_name = dcm_path.split('/')[-2]
            ppid = dcm_folder_name[9:dcm_folder_name.rfind('T')-1]
            fout.write(ppid + '\n')

fout.close()



pydicom.read_file('', stop_before_pixels=)