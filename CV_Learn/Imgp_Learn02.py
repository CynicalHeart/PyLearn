# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 22:05
# @Author  : Wu Tianyu
# 几何变换
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 扩展缩放
def resize_learn():
    res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    height, width = img.shape[:2]
    # res = cv2.resize(img, (height * 2, width * 2), interpolation=cv2.INTER_LINEAR)  # 效果同上
    while True:
        cv2.imshow("res", res)
        cv2.imshow("img", img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


# 仿射变换
def warp_Affine():
    rows, cols, ch = img.shape
    pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    pts2 = np.float32([[10, 100], [400, 50], [100, 400]])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    plt.subplot(121), plt.imshow(img), plt.title('input')
    plt.subplot(122), plt.imshow(dst), plt.title('output')
    plt.show()


# 旋转
def warp_Rotation():
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)
    dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
    while True:
        cv2.imshow("rotation", dst)
        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()


# 透视变化
def warp_perspective():
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (300, 300))
    plt.subplot(121), plt.imshow(img), plt.title('input')
    plt.subplot(122), plt.imshow(dst), plt.title('output')
    plt.show()


if __name__ == '__main__':
    img = cv2.imread("img/67814952_p0_master1200.jpg")
    # resize_learn()
    # warp_Rotation()
    # warp_Affine()
    warp_perspective()
