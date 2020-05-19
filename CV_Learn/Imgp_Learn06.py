# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 12:07
# @Author  : Wu Tianyu
# 图像梯度
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 对比Sobel,Scharr,Laplacian三种滤波器的效果
def grad_Compare():
    img = cv2.imread('img/67814952_p0_master1200.jpg', 0)
    laplacian = cv2.Laplacian(img, cv2.CV_16S)
    laplacian_abs = cv2.convertScaleAbs(laplacian)
    sobel_x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3)
    sobel_x_abs = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3)
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Origin')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian_abs, cmap='gray'), plt.title('laplacian')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobel_x_abs, cmap='gray'), plt.title('sobel_x')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobel_y_abs, cmap='gray'), plt.title('sobel_y')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    grad_Compare()
