#!/usr/bin/python3
'''
# @Time    : 2020/11/22 21:29
# @Author  : raymond
# @Email   : rayxie0623@163.com
# @File    : test_handlerdb.py
# @Software: PyCharm
'''
from unittest import TestCase
from studentmanager.handlerdb import Handler_Db


class TestHandler_Db(TestCase):
    def test_add(self):
        hd = Handler_Db()
        sql = "insert into class_15 (id, name) values (%s, %s)"
        val = (2, "崔珂铭")
        hd.add(sql, val)

    def test_delete(self):
        hd = Handler_Db()
        sql = "delete from class_15 where name = '崔珂铭'"
        hd.delete(sql)

    def test_update(self):
        hd = Handler_Db()
        sql = "update class_15 set name = %s where name = %s"
        val = ("王三", "赵凌睿")
        hd.update(sql, val)

    def test_query(self):
        hd = Handler_Db()
        sql = "select * from class_15"
        hd.query(sql)

    def test_add_item(self):
        hd = Handler_Db()
        id = 3
        name = "黄乔"
        hd.add_item(id, name)

    def test_delete_by_id(self):
        hd = Handler_Db()
        hd.delete_by_id(6)
        hd.delete_by_id(1)

    def test_delete_by_name(self):
        hd = Handler_Db()
        hd.delete_by_name("谢佳男")
        hd.delete_by_name("黄乔")

    def test_update_by_id(self):
        hd = Handler_Db()
        old_id = 3
        new_id = 4
        hd.update_by_id(old_id, new_id)


    def test_update_by_name(self):
        hd = Handler_Db()
        old_name = '黄乔'
        new_name = '小仙女'
        hd.update_by_name(old_name, new_name)

    def test_query_by_id(self):
        hd = Handler_Db()
        hd.query_by_id(6)
        hd.query_by_id(1)


    def test_query_by_name(self):
        hd = Handler_Db()
        hd.query_by_name("谢佳男")
        hd.query_by_name("王三")