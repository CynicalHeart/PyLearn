# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 20:39
# @Author  : Wu Tianyu
# 图像金字塔
import cv2


# 高斯金字塔
def GaussianPyr():
    img = cv2.imread("img/67814952_p0_master1200.jpg")
    rows, cols = img.shape[:2]
    lower_reso = cv2.pyrDown(img, (rows // 2, cols // 2))  # 分辨率降低向上构建金字塔
    high_reso = cv2.pyrUp(img)
    cv2.imshow("lower_reso", lower_reso)
    cv2.imshow("high_reso", high_reso)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    GaussianPyr()
