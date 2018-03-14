#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '深度学习 卷积'
__author__ = 'JN Zhang'
__mtime__ = '2018/3/14'
"""
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

from matplotlib import pyplot as plt

from keras.datasets import mnist


if __name__ == "__main__":
    # 从 MNIST 加载图片数据
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # 查询数据集
    print(x_train.shape)
    plt.imshow(x_train[0])

