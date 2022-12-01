import math
import cv2 as cv

def hough_lines():
    src = cv.imread('./images/building.jpg', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    edge = cv.Canny(src, 50, 150)
    lines = cv.HoughLines(edge, 1, math.pi / 180, 250)
    dst = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    if lines is not None:
        for i in range(lines.shape[0]):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            cos_t = math.cos(theta)
            sin_t = math.sin(theta)
            x0, y0 = rho * cos_t, rho * sin_t
            alpha = 1000
            pt1 = (int(x0 - alpha * sin_t), int(y0 + alpha * cos_t))
            pt2 = (int(x0 + alpha * sin_t), int(y0 - alpha * cos_t))
            cv.line(dst, pt1, pt2, (0, 0, 255), 2, cv.LINE_AA)


    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

hough_lines()