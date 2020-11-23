#!/usr/bin/python3
'''
# @Time    : 2020/11/22 10:35
# @Author  : raymond
# @Email   : rayxie0623@163.com
# @File    : handlerdb.py
# @Software: PyCharm
'''

import pymysql
from studentmanager.readconfig import ReadConfig


class Handler_Db(object):

    def __init__(self):
        self.conf = ReadConfig()

    def conn_mysql(self):
        '''
        连接数据库
        :return:
        '''
        config = {
            # 'host': '192.168.109.34',
            'host': self.conf.get_db('host') or '127.0.0.1',
            'port': 3306,
            'user': self.conf.get_db('user') or 'root',
            'password': self.conf.get_db('password') or 'root',
            'db': self.conf.get_db('db'),
            'charset': self.conf.get_db('charset') or 'utf8'
        }
        try:
            self.conn = pymysql.connect(**config)
            self.cur = self.conn.cursor()
        except pymysql.err as e:
            print("数据库连接失败", str(e))
        else:
            print("mysql数据库连接成功")

    def excute_sql(self, sql, var=None):
        '''
        执行响应的sql
        :param sql:
        :param var:
        :return:
        '''
        self.conn_mysql()
        self.cur.execute(sql, var)
        self.conn.commit()

    def close_mysql(self):
        '''
        关闭数据库
        :return:
        '''
        self.cur.close()
        self.conn.close()

    def add(self, sql, var):
        '''
        插入
        :param sql:
        :param var:
        :return:
        '''
        self.excute_sql(sql, var)
        print("数据库插入成功")
        self.close_mysql()

    def delete(self, sql):
        '''
        删除
        :param sql:
        :return:
        '''
        self.excute_sql(sql)
        print("删除成功")
        self.close_mysql()

    def update(self, sql, var):
        '''
        改
        :param sql:

        :return:
        '''
        self.excute_sql(sql, var)
        print("更改成功")
        self.close_mysql()

    def query(self, sql):
        '''
        查询
        :param sql:
        :return:
        '''
        self.excute_sql(sql)
        res_vals = self.cur.fetchall()
        for res_val in res_vals:
            print(res_val)
        return res_vals

    #todo
    '''
    1. 在进行增删该查前都应该先判断是否存在，不然应该报错
    2. 改进如下:
    add: 
        1. 判断是否存在： 完成
            根据id
    delete:
        2. 判断是否存在
            根据id删除 完成
            根据名字删除 完成
        删除后id得重新排
    update:
        1.判断是否存在
            根据id 
            根据名字：
                判断更新后的id是否存在 
    query:
        1.提供根据id和名字查询
        2.判断是否存在
    '''
    def add_item(self, id, name):
        if not self.query_by_id(id):
            sql = "insert into class_15 (id, name) values (%s, %s)"
            val = (id, name)
            self.add(sql, val)

    def delete_by_id(self, id):
        if self.query_by_id(id):
            sql = "delete from "+self.conf.get_db("table15")+" where id = " + str(id)
            self.delete(sql)

    def delete_by_name(self, name):
        if self.delete_by_name(name):
            sql = "delete from "+self.conf.get_db("table15")+" where name = " + "'"+ name +"'"
            self.delete(sql)

    def update_by_id(self, old_id, new_id):
        if self.query_by_id(old_id):
            sql = "update class_15 set id = %s where id = %s"
            print(sql)
            val = (new_id, old_id)
            self.update(sql, val)

    def update_by_name(self, old_name, new_name):
        if self.query_by_name(old_name):
            sql = "update class_15 set name = %s where name = %s"
            val = (new_name, old_name)
            self.update(sql, val)

    def query_by_id(self, id):
        sql = "select * from " + self.conf.get_db("table15") + " where id = " + str(id)
        # print(sql)
        if not self.query(sql):
            print("id不存在")
            return False
        return True

    def query_by_name(self, name):
        sql = "select * from " + self.conf.get_db("table15") + " where name = " + "'"+ name +"'"
        # print(sql)
        if not self.query(sql):
            print(name + "不存在")
            return False
        return True