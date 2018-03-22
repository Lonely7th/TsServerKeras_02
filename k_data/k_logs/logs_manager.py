#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'JN Zhang'
__mtime__ = '2018/3/22'
"""
import logging

import os


class LogsManager:
    def __init__(self, flags):
        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        log_path = os.path.dirname(os.getcwd()) + "/"
        log_name = log_path + flags + '.log'
        logfile = log_name
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

        # 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
