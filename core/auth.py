# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:05
# @Author  : Jie Ke Man
# @FileName: auth.py
# @Software: PyCharm
'''用户认证模块'''
import os
import json
import time
from conf import setting
from core import db_handler


def acc_auth(account, password):
    '''
    account auth func
    :param account:
    :param password:
    :return:
    '''
    db_path = db_handler.db_handler(setting.DATE_BASE)
    account_file = '%s/%s.json' % (db_path, account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file, 'r')as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(
                    account_data['expire_date'], '%Y-%m-%d'))
                if time.time() > exp_time_stamp:
                    print('1mAccount[%s] has expired')
                else:
                    return account_data
            else:
                print('1mAccount ID or password is incorrect')
    else:
        print('1mAccount [%s] does not exist!' % account)


def acc_login(user_data, log_obj):
    '''
    account login func
    :param user_data:
    :param log_obj:
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input('\033[32:1maccount:\033[0m').strip()
        password = input('\033[32:1mpassword:\033[0m').strip()
        auth = acc_auth(account, password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            print('welcome')
            return auth
        retry_count += 1
    else:
        log_obj.error('account [%s] too many login attempts' % account)
        exit()
