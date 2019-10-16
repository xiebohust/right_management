# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:07
# @Author  : Jie Ke Man
# @FileName: transaction.py
# @Software: PyCharm
'''记账,还钱,取钱等所有与账户金额相关操作'''
import json
from conf import setting
from core import account


def make_transaction(log_obj, account_data, tran_type, amount, **other):
    amount = float(amount)
    if tran_type in setting.TRANSACTION_TYPE:
        interest = amount * setting.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if setting.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif setting.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('your credit is not enough')
                return
        account_data['balance'] = new_balance
        account.dump_account(account_data)
        log_obj.info('account:%s   action:%s  amount:%s interest:%s'
                     % (account_data['id'], tran_type, amount, interest))
        return account_data

    else:
        print('not transaction type')
