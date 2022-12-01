import numpy as np
import cv2 as cv

def sobel_edge():
    src = cv.imread('./images/lenna.bmp', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    dx = cv.Sobel(src, cv.CV_32F, 1, 0)
    dy = cv.Sobel(src, cv.CV_32F, 0, 1)

    print(dx)
    print(dy)

    fmag = cv.magnitude(dx, dy) # fmag : 그래디언트 크기
    mag = np.uint8(np.clip(fmag, 0, 255)) # fmag 포화 연산 수행 -> mag
    _, edge = cv.threshold(mag, 150, 255, cv.THRESH_BINARY) # 150보다 크면 255(흰색), 아니면 0(검은색)

    cv.imshow('src', src)
    cv.imshow('mag', mag)
    cv.imshow('edge', edge)
    cv.waitKey()
    cv.destroyAllWindows()

sobel_edge()