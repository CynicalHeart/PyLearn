# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 22:08
# @Author  : Wu Tianyu
# 视频
import numpy as np
import cv2


def read_video():
    cap = cv2.VideoCapture(0)
    while True:
        rat, frame = cap.read()  # 第一个参数ret 为True 或者False,代表有没有读取到图片
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()  # 释放
    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_video()
