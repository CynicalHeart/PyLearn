# -*- coding: utf8 -*-
# @Time    : 2020/5/9 20:46
# @Author  : Wu Tianyu
# 图片
import numpy as np
from matplotlib import pyplot as plt
import cv2


def cv_test01():
    img = cv2.imdecode(np.fromfile("F:\\腾讯\\图\\80780817_p0.png", dtype='uint8'), -1)
    if img is None:
        print("图片路径错误")
    cv2.namedWindow("image show", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image show", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite("D:\\flower.png", img)
        cv2.destroyAllWindows()


def cv_test02():
    img = cv2.imdecode(np.fromfile("F:\\腾讯\\图\\80780817_p0.png", dtype='uint8'), -1)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__ == '__main__':
    cv_test02()
