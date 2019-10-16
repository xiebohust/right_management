# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:07
# @Author  : Jie Ke Man
# @FileName: main.py
# @Software: PyCharm
# 主逻辑交互程序
from core import account
from core import auth
from core import logger
from core import transaction
# transaction logger
trans_logger = logger.logger('transaction')
# access logger
access_logger = logger.logger('access')


def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :param acc_data:
    :return:
    '''
    account_data = account.load_current_balance(acc_data['account_id'])
    current_balance = '''-------BALANCE INFO------
        Credit: %s
        Balance: %s
    ''' % (acc_data['credit'], acc_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('input repay amount:').strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(
                trans_logger, account_data, 'repay', repay_amount)


def account_info():
    print(user_data)


def withdraw():
    pass


def transfer():
    pass


def pay_check():
    pass


def logout():
    pass


def interactive(acc_data):
    '''
    interact with user
    :param acc_data:
    :return:
    '''
    menu = u'''
    ------oldboy bank------
    1m1.账户信息
    2.还款
    3.取款
    4.转账
    5.账单
    6.退出
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,

    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>>:').strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
            print('option does not exist')


user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def run():
    '''需要用户先认证'''
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
