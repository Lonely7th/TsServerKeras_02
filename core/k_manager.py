#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '卷积运算'
__author__ = 'JN Zhang'
__mtime__ = '2018/3/14'
"""
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Convolution2D
from keras.utils import np_utils

from matplotlib import pyplot as plt

from keras.datasets import mnist


if __name__ == "__main__":
    # 从 MNIST 加载图片数据
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # 查询数据集
    # print(x_train.shape)
    # plt.imshow(x_train[0])
    # plt.show()
    # 数据预处理，显式地声明一个维度，用于表示输入图片的深度
    x_train = x_train.reshape(x_train.shape[0], 1, 28, 28)
    x_test = x_test.reshape(x_test.shape[0], 1, 28, 28)
    # 将数据类型转换成float32，使值落在[0, 1]之间
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    # 标签预处理，由于我们的训练数据是MNIST(数字图片)，最终应该将这些图片分成10个类别(0-9)
    # 这里我们将标签处理成10个不同的类型，每个类型代表一个数字
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    # 定义模型架构
    # 声明一个顺序模型
    model = Sequential()
    # 声明一个输入层
    model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(1, 28, 28)))
    print(model.output_shape)

