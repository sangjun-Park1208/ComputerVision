import math
import numpy as np
import cv2 as cv

def hough_lines():
    src = cv.imread('./images/building.jpg', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    edge = cv.Canny(src, 50, 150)
    lines = cv.HoughLinesP(edge, 1, math.pi / 180, 160, minLineLength=50, maxLineGap=5)
    dst = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(dst, pt1, pt2, (0, 0, 255), 2, cv.LINE_AA)


    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

hough_lines()