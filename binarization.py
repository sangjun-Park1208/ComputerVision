import numpy as np
import cv2 as cv



def binarization():
    src = cv.imread('./images/neutrophils.png', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    cv.imshow('src', src)

    def threshold():
        _, dst = cv.threshold(src, 128, 255, cv.THRESH_BINARY)
        cv.imshow('dst', dst)
        cv.waitKey()
        cv.destroyAllWindows()


    threshold()

binarization()