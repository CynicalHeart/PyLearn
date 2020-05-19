# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 21:53
# @Author  : Wu Tianyu
# 霍夫变换
import numpy as np
import cv2


# 标准霍夫变换
def hough_line():
    img = cv2.imread("img/build.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # 绘制直线
    for line in lines:
        rho = line[0][0]
        theta = line[0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("build_line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 累计概率霍夫变换 (优秀)
def hough_lineP():
    img = cv2.imread("img/build.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    minLineLength = 80
    maxLineGap = 5
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=minLineLength, maxLineGap=maxLineGap)
    for line in lines:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[0][2], line[0][3]
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
    cv2.imshow("build_lineP", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 霍夫圆
def hough_circle():
    img = cv2.imread("img/cv_logo.jpg", 0)
    img = cv2.medianBlur(img, 5)
    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=100, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))  # np.around 对矩阵列表四舍五入
    print(circles)
    for circle in circles[0, :]:
        # 绘制圆心
        cv2.circle(color_img, (circle[0], circle[1]), 2, (255, 0, 255), -1)
        # 绘制轮廓
        cv2.circle(color_img, (circle[0], circle[1]), circle[2], (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("detect circle", color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # hough_line()
    # hough_lineP()
    hough_circle()
