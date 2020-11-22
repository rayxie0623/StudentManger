#!/usr/bin/python3
'''
# @Time    : 2020/11/22 20:43
# @Author  : raymond
# @Email   : rayxie0623@163.com
# @File    : test_readconfig.py
# @Software: PyCharm
'''
from unittest import TestCase
from studentmanager.readconfig import ReadConfig


class TestReadConfig(TestCase):
    def test_get_db(self):
        rc = ReadConfig()
        db_url = rc.get_db("host")
        print("db_url :" + db_url)
        db_port = rc.get_db("port")
        print("db_port :" + db_port)
