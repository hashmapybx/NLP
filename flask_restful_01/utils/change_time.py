#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15/0015 22:37
# @Author  : Mat
import datetime
import os
import shutil
import time

import pydicom

def find_dicom(path):
    save_path = path + '_new'
    pici_time = path.split('/')[-1][:10]
    pi_time_time = int(time.mktime(datetime.datetime.strptime(pici_time, '%Y_%m_%d').timetuple()))

    for dirpath, dirname, filenames in os.walk(path):
        for dcm in filenames:
            dcm_path = os.path.join(dirpath, dcm)
            if dcm_path.endswith('.dcm'):
                info = pydicom.read_file(dcm_path, force=True, stop_before_pixels=True)
                try:
                    studyDate = info.StudyDate
                    studyDate_time = int(time.mktime(datetime.datetime.strptime(studyDate, '%Y%m%d').timetuple()))
                    if studyDate_time > (pi_time_time - 3600 * 24 * 10):
                        dcm_tail = os.path.split(dcm_path)[-1]
                        dcm_dir =  os.path.split(dcm_path)[0].replace(path, '')
                        out_path = save_path + dcm_dir
                        if not os.path.exists(out_path):
                            os.makedirs(out_path)
                        shutil.move(dcm_path, os.path.join(out_path, dcm_tail))
                except:
                    print(dcm_path)
                    pass


if __name__ == '__main__':
    path = '/media/tx-eva-data/NAS/原始数据库/肺部计算机辅助诊断软件/CE021008/2018_06_19_CE021008_data_need_change_time'
    save_path = path + '_new'
    path_1 = path + '/a/b/c/1.2.3.4.dcm'
    pici_time = path.split('/')[-1][:10]
    dcm_tail = os.path.split(path_1)[-1]
    dcm_dir = os.path.split(path_1)[0].replace(path, '')
    out_path = save_path + dcm_dir
    print(path_1)
    print(os.path.join(out_path, dcm_tail))
    print(pici_time)
