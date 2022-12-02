import random

import numpy as np
import cv2 as cv

def q2():
    src = cv.imread('./images/diceAll.jpg', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    contours, _ = cv.findContours(src, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    print(len(contours))
    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    for i in range(len(contours)):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.drawContours(dst, contours, i, c, 2)

    # idx = 0
    # while idx >= 0:
    #     c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #     cv.drawContours(dst, contours, idx, c, -1, cv.LINE_8, hierarchy)
    #     idx = hierarchy[0, idx, 0]

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

q2()