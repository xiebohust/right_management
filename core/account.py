# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:04
# @Author  : Jie Ke Man
# @FileName: account.py
# @Software: PyCharm
'''用于文件加载和存储的账户数据'''
import json
from core import db_handler
from conf import setting


def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    db_path = db_handler.db_handler(setting.DATE_BASE)
    account_file = '%s/%s.json' % (db_path, account_id)
    with open(account_file)as f:
        acc_data = json.load(f)
        return acc_data


# def dump_account(account_data):
