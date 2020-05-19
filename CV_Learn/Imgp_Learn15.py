# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 13:59
# @Author  : Wu Tianyu
# GrabCut
import numpy as np
from matplotlib import pyplot as plt
import cv2


def grab_cut():
    img = cv2.imread("img/t_lu.jpg")
    mask = np.zeros(img.shape[:2], np.uint8)
    bdgModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (10, 0, 180, 184)
    cv2.grabCut(img, mask, rect, bdgModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    plt.imshow(img), plt.colorbar(), plt.show()


if __name__ == '__main__':
    grab_cut()
