# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 20:20
# @Author  : Wu Tianyu
# 阈值
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 五种阈值演示
def threshold_test():
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    titles = ['Origin', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(0, 6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


# 自适应阈值
def adaptive_threshold():
    global img
    # 中值滤波
    img = cv2.medianBlur(img, 5)
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # 自适应阈值 取邻域平均值
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # 取邻域加权和
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    titles = ['Origin Image', 'Global Threshold(127)', 'Adaptive Mean Threshold', 'Adaptive GAUSSIAN Threshold']
    images = [img, thresh, th1, th2]
    for i in range(0, 4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


# Otsu's 二值化
def otsu_binary():
    # 全局阈值
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # otsu's 阈值 (阈值设为0)
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 高斯滤波
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Origin Noisy', 'hist', 'Global(127)',
              'Origin Noisy', 'hist', "Otsu's",
              'Gaussian filter', 'hist', "Otsu's"]
    for i in range(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img = cv2.imread("img/chouyou.jpg", 0)
    # threshold_test()
    # adaptive_threshold()
    otsu_binary()
