# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:08
# @Author  : Jie Ke Man
# @FileName: account_sample.py
# @Software: PyCharm
# 生成一个初始账户数据
import json
acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date':'2016-01-02',
    'expire_date':'2021-01-01',
    'status':0 # 0表示正常

    }
acc_dic2 = {
    'id': 2345,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date':'2016-01-02',
    'expire_date':'2021-01-01',
    'status':0 # 0表示正常

    }
with open(r"account\1234","w") as file:
    json.dump(acc_dic,file)

with open(r"account\2345","w") as file:
    json.dump(acc_dic2,file)
