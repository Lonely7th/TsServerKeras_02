#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '绘图工具'
__author__ = 'JN Zhang'
__mtime__ = '2018/3/26'
"""
import numpy as np
import matplotlib.pyplot as pylt


class DrawUtils:
    def __init__(self):
        self.plt = pylt.figure(figsize=(8, 6), dpi=80)
        self.plt.subplots(111)
        pass

    # 绘制折线图
    def draw_plt(self, plt, data_list, title='', color="r"):
        lable_x = np.arange(len(data_list))
        # 绘制K线
        plt.plot(lable_x, data_list, color=color, linewidth=1.0, linestyle="-")
        plt.xlim(lable_x.min(), lable_x.max() * 1.1)
        plt.ylim(min(data_list) * 0.9, max(data_list) * 1.1)
        plt.title(title)
        plt.grid(True)
