# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:06
# @Author  : Jie Ke Man
# @FileName: logger.py
# @Software: PyCharm
'''日志记录模块'''
import logging
from conf import setting


def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)
    # create console handle and set level to info
    ch = logging.StreamHandler()
    ch.setLevel(setting.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = '%s/log/%s' % (setting.BASE_DIR, setting.LOG_TYPE)
    fh = logging.FileHandler(log_file)
    fh.setLevel(setting.LOG_LEVEL)
    # creat formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s')
    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
