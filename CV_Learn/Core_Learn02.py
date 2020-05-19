# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 20:26
# @Author  : Wu Tianyu
# 程序性能检测及优化
import numpy as np
import cv2


# getTickFrequency 和 getTickCount
def getTick():
    e1 = cv2.getTickCount()
    for i in range(5, 10, 2):
        img_src = cv2.medianBlur(img, i)
        cv2.imshow("median%d" % i, img_src)
    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()
    print(time)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = cv2.imread("img/chouyou.jpg")
    getTick()
