import cv2 as cv

def q3():
    src = cv.imread('./images/case3/img3_1.png', cv.IMREAD_GRAYSCALE)
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


    # 침식
    erode = cv.erode(binarization, None)
    erode = cv.erode(erode, None)
    cv.imshow('erode', erode)

    contours, hierarchy = cv.findContours(erode, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    dst = cv.cvtColor(erode, cv.COLOR_GRAY2BGR)

    idx = 0
    i = 1
    ans = []

    while idx >= 0:
        addnum = 0
        while i < len(contours):
            if hierarchy[0, i, 2] < 0: # 자식 객체 외곽선
                addnum += 1
                i += 1
                continue
            i += 1
            break
        cv.drawContours(dst, contours, idx, (0, 0, 255), 2, cv.LINE_8, hierarchy)
        idx = hierarchy[0, idx, 0]
        if addnum == 0:
            continue
        ans.append(addnum)

    ans.sort()
    print(ans)
    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

q3()
