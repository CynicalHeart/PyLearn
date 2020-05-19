# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 20:17
# @Author  : Wu Tianyu
# 边缘检测
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 边缘检测 canny
def canny_test():
    img = cv2.imread('img/chouyou.jpg', 0)
    edges = cv2.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Origin')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray'), plt.title('Canny')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    canny_test()
