import math

import cv2 as cv

def q5():
    src = cv.imread('./images/case5/img5_7.png', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    # 양방향 필터
    filtered = cv.bilateralFilter(src, -1, 15, 15)
    cv.imshow('filtered', filtered)

    # 히스토그램 스트레칭
    gmin, gmax, _, _ = cv.minMaxLoc(filtered)
    stretch = cv.convertScaleAbs(filtered, alpha=255.0/(gmax - gmin), beta=-gmin * 255.0/(gmax - gmin))
    cv.imshow('stretch', stretch)

    # 이진화
    _, binarization = cv.threshold(stretch, 185, 255, cv.THRESH_BINARY)
    cv.imshow('binarization', binarization)

    contours, hierarchy = cv.findContours(binarization, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    dst = cv.cvtColor(binarization, cv.COLOR_GRAY2BGR)

    ans = 0
    idx = 0
    for pts in contours:
        if cv.contourArea(pts) < 400:
            idx += 1
            continue

        approx = cv.approxPolyDP(pts, cv.arcLength(pts, True)*0.02, True)
        vtc = len(approx)

        if vtc == 3:
            idx += 1
            continue
        elif vtc == 4:
            idx += 1
            continue
        else:
            length = cv.arcLength(pts, True)
            area = cv.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)
            if ratio > 0.85:
                cv.drawContours(dst, contours, idx, (0, 0, 255), 2, cv.LINE_8, hierarchy)
                ans += 1
            idx += 1

    print(ans)
    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

q5()