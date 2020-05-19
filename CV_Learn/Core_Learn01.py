# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 19:17
# @Author  : Wu Tianyu
# 图像基础操作
import numpy as np
from matplotlib import pyplot as plt
import cv2


# 修改像素值
def change_p():
    print(img[100, 100])
    img[100, 100] = [255, 255, 255]
    print(img[100, 100])
    print(img.item(10, 10, 2))
    img.itemset((10, 10, 2), 100)
    print(img.item(10, 10, 2))


# 获取图像的属性
def get_attr():
    print(img.shape)  # 返回行、列、通道数
    print(img.size)  # 返回图像像素的数目
    print(img.dtype)  # 返回图像的数据类型


# ROI (切片)
def ROI():
    img_roi = img[0:400, 750:1150]
    cv2.imshow("origin", img)
    cv2.imshow("ROI", img_roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 拆分并合并通道
def SplitAndMerge():
    global img
    b, g, r = cv2.split(img)
    cv2.imshow("B", b)
    cv2.imshow("G", g)
    cv2.imshow("R", r)
    img = cv2.merge((b, g, r))
    # 也可以使用np的索引改变通道:img[:,:,2] = 0
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 为图像扩充边(填充)
def border_mark():
    BLUE = [255, 0, 0]
    replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

    plt.subplot(231), plt.imshow(img, 'gray'), plt.title('origin')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('replicate')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('reflect')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('reflect101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('wrap')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('constant')
    plt.show()


if __name__ == '__main__':
    img = cv2.imdecode(np.fromfile("F:\\腾讯\\图\\chouyou.jpg", dtype='uint8'), -1)
    border_mark()
