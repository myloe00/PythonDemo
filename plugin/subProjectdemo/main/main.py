# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: main.py
# @Author: myloe
# @Time: Nov 06, 2020
# ---
import sys
from tool.conf_file import conf_file
import os


def get_datasource():
    return conf_file.common.datasource


if __name__ == '__main__':

    print("xxxx")
    print(os.path.abspath(get_datasource()))
