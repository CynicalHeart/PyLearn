# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 21:24
# @Author  : Wu Tianyu
# 颜色空间转换
import numpy as np
import cv2


# 蓝色追踪(物体追踪)
def blue_catch():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 设定蓝色的阈值
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        # 构建mask
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # 与运算
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        key = cv2.waitKey(5)
        if key == 27:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    blue_catch()
