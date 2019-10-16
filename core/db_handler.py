# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:06
# @Author  : Jie Ke Man
# @FileName: db_handler.py
# @Software: PyCharm
'''数据库连接引擎'''


def file_db_handle(conn_params):
    '''
    parse the db file path
    :param conn_params:
    :return:
    '''
    print('file db', conn_params)
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])
    return db_path


def db_handler(conn_paramms):
    '''
    connect to db
    :param conn_paramms:
    :return:
    '''
    if conn_paramms['engine'] == 'file_storage':
        return file_db_handle(conn_paramms)
