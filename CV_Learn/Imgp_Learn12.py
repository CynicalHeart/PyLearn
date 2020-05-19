# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 19:54
# @Author  : Wu Tianyu
# 模板匹配
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 模板匹配
def template():
    src_img = cv2.imread("img/kailu.jpg", 0)
    img = src_img.copy()
    temp = cv2.imread("img/t_lu.jpg", 0)
    w, h = temp.shape[::-1]
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
               'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    for mod in methods:
        src_img = img.copy()
        method = eval(mod)  # eval 用来计算存储在字符串的有效py表达式
        res = cv2.matchTemplate(src_img, temp, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(src_img, top_left, bottom_right, 255, 2, cv2.LINE_AA)

        plt.subplot(121), plt.imshow(res, cmap='gray'), plt.title('Matching')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(src_img, cmap='gray'), plt.title('Detected')
        plt.xticks([]), plt.yticks([])
        plt.suptitle(mod)
        plt.show()


if __name__ == '__main__':
    template()
