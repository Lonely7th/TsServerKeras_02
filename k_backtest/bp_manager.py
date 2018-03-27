#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '回测管理类'
__author__ = 'JN Zhang'
__mtime__ = '2018/3/26'
"""
import multiprocessing
import time
import pandas as pd

from datetime import datetime


def creat_calendar(__start_date, __end_date):
    date_l = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=__start_date, end=__end_date))]
    return date_l


class BackProbeManager:
    def __init__(self, start_date, end_date, fun_buy, fun_sell, base_capital=100000, fun_add_space=None, fun_delete_space=None):
        self.start_date = start_date
        self.end_date = end_date
        self.fun_buy = fun_buy
        self.fun_sell = fun_sell
        self.base_capital = base_capital
        self.fun_add_space = fun_add_space
        self.fun_delete_space = fun_delete_space
        self.__process = multiprocessing.Process(target=self.run_bp, args=())

    def start_bp(self):
        self.__process.start()
        self.__process.join()

    def run_bp(self):
        """
        判断数据格式
        """
        if self.fun_buy is None or self.fun_sell is None:
            print("缺少主要逻辑")
            return
        try:
            time.strptime(self.start_date, "%Y-%m-%d")
            time.strptime(self.end_date, "%Y-%m-%d")
        except Exception as e:
            print("时间格式错误")
            print(e)
            return
        """
        模拟时间进程
        """
        __calendar = creat_calendar(self.start_date, self.end_date)
        for date in __calendar:
            print(date)
        """
        输出回测结果
        """

    def stop_bp(self):
        self.__process.terminate()


if __name__ == "__main__":
    bpm = BackProbeManager("2017-02-03", "2017-08-20", creat_calendar, creat_calendar)
    bpm.start_bp()
    bpm.stop_bp()
