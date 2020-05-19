# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 20:17
# @Author  : Wu Tianyu
# 直方图
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 绘制灰度直方图
def calc_test():
    img = cv2.imread("img/ren.jpg", 0)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])  # 256个bin
    # 绘制直方图
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


# 三色绘制直方图
def calc_test02():
    img = cv2.imread("img/ren.jpg")
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()


# 使用掩膜的直方图
def calc_mask():
    img = cv2.imread("img/ren.jpg", 0)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[100:800, 100:900] = 255
    mask_img = cv2.bitwise_and(img, img, mask=mask)
    hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(mask_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()


# 直方图均衡化
def equalize():
    img = cv2.imread("img/ren.jpg", 0)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))
    cv2.namedWindow("equalize", cv2.WINDOW_NORMAL)
    # 适应性直方图均衡化
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)
    cv2.imshow("equalize", res)
    cv2.imshow("clahe", cl1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 2D直方图
def hist_2D():
    img = cv2.imread("img/67814952_p0_master1200.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # 绘制2D直方图
    plt.imshow(hist, interpolation='nearest')
    plt.show()


# 反向投影
def back_projection():
    """
    导入roi图,target图,将他们都转化为hsv格式
    calcHist求出roi的hist,并将它normalize化(0,255)
    求出dst通过calcBackProjection,引入目标的hsv图和roi的hist
    将结果dst通过filter2D卷积使分散的点连接起来(dst,-1,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    dst阈值化结果得到thresh
    merge三个通道
    按位操作得到res
    """
    pass


if __name__ == '__main__':
    calc_test()
    # calc_test02()
    # calc_mask()
    # equalize()
    # hist_2D()
