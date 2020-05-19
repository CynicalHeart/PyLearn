# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 13:52
# @Author  : Wu Tianyu
# 鼠标操作
import numpy as np
from random import randint
import cv2


# 双击画圆回调函数
def simple_circle(event, x, y, flags, param):
    b, g, r = randint(0, 255), randint(0, 255), randint(0, 255)
    if event == cv2.EVENT_LBUTTONDBLCLK:  # 双击事件
        cv2.circle(img, (x, y), 100, (b, g, r), 1, cv2.LINE_AA)


# 简单的鼠标画笔演示
def SIM_test():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', simple_circle)
    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()


drawing = False  # 鼠标按下时变为True
mode = True  # true为矩形、false为曲线
ix, iy = -1, -1  # 初始化起点


# 圆形回调
def draw_circle(event, x, y, flags, param):
    global drawing, mode, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2, 8)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


# 高级交互式演示
def ADV_test():
    global mode
    cv2.namedWindow("image")
    cv2.setMouseCallback('image', draw_circle)
    while True:
        cv2.imshow("image", img)
        k = cv2.waitKey(1)
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break


if __name__ == '__main__':
    img = np.zeros((512, 512, 3), dtype=np.uint8)
    ADV_test()
    cv2.destroyAllWindows()
