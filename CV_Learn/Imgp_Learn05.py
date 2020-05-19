# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 11:21
# @Author  : Wu Tianyu
# 形态学转换
import numpy as np
from matplotlib import pyplot as plt
import cv2

# 定义核
kernel = np.ones((5, 5), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 结构化元素
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))


# 腐蚀
def erode_test():
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("erode", erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 膨胀
def dilate_test():
    dilation = cv2.dilate(img, kernel, iterations=1)
    plt.imshow(dilation, 'gray')
    plt.title('dilate')
    plt.show()


# 开运算 - 先腐蚀后膨胀 (消除零散的小亮斑)
def open_test():
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow("open", opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 闭运算 - 先膨胀再腐蚀 (消除前景中的小黑点)
def close_test():
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("close", closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 形态学梯度 即膨胀与腐蚀的差别(的出物体的轮廓)
def grad_test():
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("gradient", gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 礼帽【顶帽】 - 原始图像与开运算结果的差
# 黑帽 - 闭运算与原始图像的差
def TopAndBlack_hat():
    global kernel
    kernel = np.ones((9, 9), np.uint8)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    plt.subplot(1, 2, 1), plt.imshow(tophat), plt.title('tophat')
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(blackhat), plt.title('blackhat')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img = cv2.imread('img/chouyou.jpg', 0)
    # erode_test()
    # dilate_test()
    # open_test()
    # close_test()
    # grad_test()
    TopAndBlack_hat()
