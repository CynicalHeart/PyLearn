# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 11:33
# @Author  : Wu Tianyu
# 画图
import numpy as np
import cv2


# 直线
def draw_line():
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 2, 8)
    cv2.imshow("line", img)


# 矩形
def draw_rect():
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 1, 8)
    cv2.imshow("rect", img)


# 圆形
def draw_circle():
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv2.imshow("circle", img)


# 画椭圆
def draw_ellipse():
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)
    cv2.imshow("ellipse", img)


# 多边形
def draw_polylines():
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], dtype=np.int32)  # 数组数据类型必须为int32
    cv2.polylines(img, [pts], True, (255, 255, 255), 2, 8)
    cv2.imshow("polylines", img)


# 书写文字
def draw_text():
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'text', (200, 480), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("text", img)


if __name__ == '__main__':
    img = np.zeros((512, 512, 3), np.uint8)
    draw_line()
    draw_rect()
    draw_circle()
    draw_ellipse()
    draw_polylines()
    draw_text()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
