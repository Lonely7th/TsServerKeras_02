#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '数据处理工具'
__author__ = 'JN Zhang'
__mtime__ = '2018/3/26'
"""
from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient


# 用于初始化数据
def init_base_data():
    pass


class DataUtils:
    def __init__(self, table_name):
        """
        连接MongoClient
        由3种方法可以选择，看使用情况
        """
        # 指定端口和地址
        self.client = MongoClient(mod_config.get_config("database", "dbhost"), int(mod_config.get_config("database", "dbport")))

        # 选择数据库
        self.db = self.client[mod_config.get_config("database", "dbname")]
        self.table = self.db[table_name]

    def clsoe_db(self):
        self.client.close()

    def add_one(self, post, created_time=datetime.now()):
        """
        添加一条数据
        需要注意的是Mongo中不需要事先建立表，插入数据的同时直接根据所传入字典对象的内容生成表
        """
        post['created_time'] = created_time
        # 指定将数据添加到blog下的post表
        return self.table.insert_one(post)

    def find_by_id(self, tk_code, request={}):
        """
        通过tk_code查找数据
        """
        if tk_code:
            request["code"] = tk_code
            return self.table.find_one(request)
        else:
            # 数据量较大时避免CursorNotFoundException
            return self.table.find({}, no_cursor_timeout=True)

    def add_tk_item(self, tk_code, price_item):
        """
        向详情列表中插入一条数据
        在update_one函数中，通过第一个参数查找更新对象，通过第二个参数对查找到的对象进行更新
        下面语句的含义是对指定ID的数据的number字段加上一个number值,通过 $inc 实现
        """
        return self.table.update_one({'code': tk_code}, {"$push": {"price_list": price_item}})

    def update_tk_item(self, tk_code, update_item):
        """
        更新数据
        update_many函数参数的作用同update_one
        {} 表示没有查找限制，更新全部的数据
        """
        return self.table.update({"code": tk_code}, {"$set": update_item})

    def update_tk_price_list(self, tk_code, cur_timer, cur_item):
        return self.table.update({"code": tk_code, "price_list.cur_timer": cur_timer}, {"$set": {"price_list.$": cur_item}})

    def delete_by_id(self, post_id):
        """
        根据ID删除，同样注意id值的格式
        """
        return self.table.delete_one({'_id': ObjectId(post_id)})


if __name__ == "__main__":
    pass
