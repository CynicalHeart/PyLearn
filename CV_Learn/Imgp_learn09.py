# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 21:03
# @Author  : Wu Tianyu
# 轮廓
import numpy as np
import cv2


# 寻找并绘制轮廓
def Contours():
    img = cv2.imread("img/67814952_p0_master1200.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    # 寻找轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 绘制轮廓
    img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("contours", img)
    ending()


# 矩:重心、面积、周长
def moment():
    img = cv2.imread("img/67814952_p0_master1200.jpg", 0)
    rows, cols = img.shape[:2]
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    M = cv2.moments(cnt)  # 计算该轮廓的矩
    print(M)
    # 计算矩的重心
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    print("矩的重心 cx:", cx, ',cy:', cy)
    # 计算轮廓的面积
    area = cv2.contourArea(cnt)
    # 计算轮廓的周长
    perimeter = cv2.arcLength(cnt, True)  # True表示闭合
    print('轮廓的面积:', area, '轮廓的周长:', perimeter)
    # 图像平均灰度
    mean_val = cv2.mean(img)
    print("图像平均灰度", mean_val)
    # 轮廓近似 (由更少的点组成的轮廓形状)
    epsilon = 0.1 * cv2.arcLength(cnt, True)  # 设置从原始轮廓到近似轮廓的最大距离
    approx = cv2.approxPolyDP(cnt, epsilon, True)  # True表闭合
    # 凸包
    hull = cv2.convexHull(cnt, clockwise=True)
    image = np.zeros((rows, cols), np.uint8)
    image = cv2.polylines(image, [hull], True, (255, 255, 255), 2, cv2.LINE_AA)
    k = cv2.isContourConvex(cnt)  # 判断是否是凸包
    print("是否是凸包", k)
    cv2.imshow("convex", image)
    ending()


# 多边形将轮廓包围
def poly_around():
    img = cv2.imread("img/67814952_p0_master1200.jpg", 0)
    rows, cols = img.shape[:2]
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image1 = np.zeros((rows, cols, 3), np.uint8)
    image2 = np.zeros((rows, cols, 3), np.uint8)
    image3 = np.zeros((rows, cols, 3), np.uint8)
    image4 = np.zeros((rows, cols, 3), np.uint8)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)  # 外部矩形边界
        img_1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (255, 255, 0), 1, cv2.LINE_AA)
        rect = cv2.minAreaRect(cnt)  # 最小包围可旋转矩形
        box = cv2.boxPoints(rect)  # 获取四个点
        box = np.int0(box)
        img_2 = cv2.drawContours(image2, [box], -1, (255, 0, 255), 1, 8)
        # 最小外接圆
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))  # 圆心
        radius = int(radius)  # 圆心
        img_3 = cv2.circle(image3, center, radius, (0, 255, 0), 1, cv2.LINE_AA)
        # 椭圆拟合
        # (x, y), (m, n), angel = cv2.fitEllipse(cnt)
        # center = (int(x), int(y))
        # axes = (int(m), int(n))
        # img_4 = cv2.ellipse(image4, center, axes, angel, 0, 360, (255, 255, 255), 2, 8)
        cv2.imshow("boundingRect", img_1)
        cv2.imshow("minAreaRect", img_2)
        cv2.imshow("minEnclosingCircle", img_3)
        # cv2.imshow("fitEllipse", img_4)
    ending()


# 凸缺陷
def hull_Defect():
    img = cv2.imread("img/67814952_p0_master1200.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[3]
    hull = cv2.convexHull(cnt, returnPoints=False)  # 查找凸缺陷，returnPoints一定是False
    defect = cv2.convexityDefects(cnt, hull)
    for i in range(defect.shape[0]):
        s, e, f, d = defect[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.line(img, start, end, (0, 255, 0), 2)
        cv2.circle(img, far, 5, (0, 0, 255), -1)
    cv2.imshow("image", img)
    ending()


def ending():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Contours()
    # moment()
    # poly_around()
    hull_Defect()
