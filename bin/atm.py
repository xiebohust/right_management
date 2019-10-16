# -*- coding: utf-8 -*-
# @Time    : 2019-9-30 14:03
# @Author  : Jie Ke Man
# @FileName: atm.py.py
# @Software: PyCharm

#  ATM执行程序

from core import main
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)


if __name__ == '__main__':
    main.run()
