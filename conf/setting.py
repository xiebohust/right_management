# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:03
# @Author  : Jie Ke Man
# @FileName: setting.py
# @Software: PyCharm
# 配置文件
# 配置文件路径,取得文件的绝对路径 os.path.abspath
import logging
import os
import sys

# 调取文件位置的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置用户存储数据  DATE_BASE
DATE_BASE = {  # 数据库
    'engine': 'file_storage',
    'name': 'account',
    'path': '%s/db' % BASE_DIR
}


# logger 文件,级别以及设置
LOG_LEVEL = logging.INFO
LOG_TYPE = {
    'transaction': 'transactions.log',
    'access': 'access.log'
}


# 操作类型 TRANSACTION_TYPE
'''repay:存钱,
    withdraw:取钱
    transfer:转账
    consume:消费
'''
TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0}
}
