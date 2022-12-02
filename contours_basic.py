import random

import numpy as np
import cv2 as cv

def canny_edge():
    src = cv.imread('./images/contours.bmp', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    contours, _ = cv.findContours(src, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)
    for i in range(len(contours)):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.drawContours(dst, contours, i, c, 2)


    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

canny_edge()