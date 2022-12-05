import cv2 as cv

def q1():
    src = cv.imread('./dice1.jpg', cv.IMREAD_GRAYSCALE)
    # src = cv.imread('./dice5.jpg', cv.IMREAD_GRAYSCALE)
    # src = cv.imread('./dice7.jpg', cv.IMREAD_GRAYSCALE)
    # src = cv.imread('./dice9.jpg', cv.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    blurred = cv.blur(src, (3, 3))
    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1, 20, param1=150, param2=30)
    dst = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    print(circles.shape[1])
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv.circle(dst, (int(cx), int(cy)), int(radius), (0, 0, 255), 2, cv.LINE_AA)

    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

q1()