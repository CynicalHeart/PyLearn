# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 12:21
# @Author  : Wu Tianyu
# 傅里叶变化
import numpy as np
from matplotlib import pyplot as plt
import cv2


def dft_test():
    img = cv2.imread("img/ren.jpg", 0)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    plt.figure(num=1)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('magnitude spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
    f_shift = dft_shift * mask
    f_ishift = np.fft.ifftshift(f_shift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    plt.figure(num=2)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('magnitude spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    dft_test()
