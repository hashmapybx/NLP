#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13/0013 11:38
# @Author  : Mat
import os
import pydicom
'''
修改检查时间是2018.08.15
如果dicom原来的检查不在2018年的 那么还需要修改age字段
birthdate = 20060201
studydate = 20160406
age = 010Y

'''

def change_time(path):
    change_time = '20180815'
    for dirpath, dirnames, filenames  in os.walk(path):
        for tfile in filenames:
            dcm_path = os.path.join(dirpath, tfile)
            if dcm_path.endswith('.dcm'):
                try:
                    info = pydicom.read_file(dcm_path, force=True)
                    ori_study_date = info.StudyDate
                    if ori_study_date.startswith('2018'):
                        info.StudyDate = change_time
                        info.SeriesDate = change_time
                        info.AcquisitionDate = change_time
                        info.ContentDate = change_time
                        info.InstanceCreationDate = change_time
                        info.save_as(dcm_path)
                    else:
                        # 修改时间的同时还是需要修改age
                        info.StudyDate = change_time
                        info.SeriesDate = change_time
                        info.AcquisitionDate = change_time
                        info.ContentDate = change_time
                        info.InstanceCreationDate = change_time
                        birthdate = info.PatientBirthDate
                        try:
                            if birthdate != '':
                                new_age = int(change_time[:4]) - int(birthdate[:4])
                                info.PatientAge = "0{}Y".format(str(new_age))
                                info.save_as(dcm_path)
                            else:
                                info.PatientBirthDate = str(int(change_time[:4])-int(info.PatientAge[:-1])) + change_time[4:]
                                info.save_as(dcm_path)

                        except:
                            print(dcm_path)
                except:
                    pass


if __name__ == "__main__":
    path = '/media/tx-eva-data/NAS/原始数据库/2.1.0.0预实验'
    change_time(path)