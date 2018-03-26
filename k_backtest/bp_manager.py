#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '回测管理类'
__author__ = 'JN Zhang'
__mtime__ = '2018/3/26'
"""


class BackProbeManager:
    def __init__(self, start_date, end_date, base_capital=100000):
        self.start_date = start_date
        self.end_date = end_date
        self.base_capital = base_capital

    def start_bp(self):
        pass

    def stop_bp(self):
        pass

    def set_action(self, fun_buy, fun_sell, fun_add_space=None, fun_delete_space=None):
        pass


if __name__ == "__main__":
    pass
