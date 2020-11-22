#!/usr/bin/python3
'''
# @Time    : 2020/11/22 20:32
# @Author  : raymond
# @Email   : rayxie0623@163.com
# @File    : readconfig.py
# @Software: PyCharm
'''
import configparser
import os


class ReadConfig(object):

    def __init__(self, filepath=None):
        if filepath:
            config_path = filepath
        else:
            #获取当前文件所在目录的上一级目录
            root_dir = os.path.dirname(os.path.abspath('.'))
            # print(root_dir)
            config_path = os.path.join(root_dir, "conf.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_db(self, param):
        value = self.cf.get("mysql-database", param)
        return value



