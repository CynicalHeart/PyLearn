# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:16
# @Author  : Wu Tianyu
# 图像平滑
import numpy as np
from matplotlib import pyplot as plt
import cv2


# filter2D卷积
def filter_2D():
    kernel = np.ones((5, 5), np.float32) / 25  # 定义核
    dst = cv2.filter2D(img, -1, kernel)
    plt.subplot(121), plt.imshow(img), plt.title('Origin')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 平滑
def blur_filter():
    blur = cv2.blur(img, (5, 5))
    plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Origin')
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 2, 2), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 高斯模糊
def gaussian_filter():
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    plt.subplot(121), plt.imshow(img), plt.title('Origin')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(gaussian), plt.title('Gaussian')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 中值滤波
def median_filter():
    median = cv2.medianBlur(img, 5)
    cv2.imshow("median filter", np.hstack((img, median)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 双边滤波
def bilateral_filter():
    image = cv2.imread('img/67814952_p0_master1200.jpg')
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    cv2.imshow("bilateral_filter", np.hstack((image, bilateral)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread('img/chouyou.jpg')
    # filter_2D()
    # blur_filter()
    # gaussian_filter()
    # median_filter()
    bilateral_filter()
