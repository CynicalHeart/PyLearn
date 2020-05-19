# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 12:24
# @Author  : Wu Tianyu
# 分水岭算法
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 分水岭
def water_shed():
    img = cv2.imread("img/coin.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)  # 去除白噪
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, 1, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, makers1 = cv2.connectedComponents(sure_fg)
    makers = makers1 + 1
    makers[unknown == 255] = 0
    makers3 = cv2.watershed(img, makers)
    img[makers3 == -1] = [255, 0, 0]
    cv2.imshow("water_shed", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    water_shed()
