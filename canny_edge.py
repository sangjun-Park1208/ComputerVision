import numpy as np
import cv2 as cv

def canny_edge():
    src = cv.imread('./images/lenna.bmp', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    dst1 = cv.Canny(src, 50, 100) # 100보다 큰 얘들은 다 edge로 검출
    dst2 = cv.Canny(src, 50, 150) # 150보다 큰 얘들은 다 edge로 검출


    cv.imshow('src', src)
    cv.imshow('dst1', dst1)
    cv.imshow('dst2', dst2)
    cv.waitKey()
    cv.destroyAllWindows()

canny_edge()