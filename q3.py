import cv2 as cv

def q2():
    src = cv.imread('./images/case3/img3_4.png', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    # 양방향 필터
    filtered = cv.bilateralFilter(src, -1, 70, 75)
    cv.imshow('filtered', filtered)

    # # 히스토그램 평활화
    # equalization = cv.equalizeHist(filtered)
    # cv.imshow('equalization', equalization)

    # 적응형 이진화
    binarization = cv.adaptiveThreshold(filtered, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 33, 10)
    cv.imshow('binarization', binarization)

    # 침식
    erode = cv.erode(binarization, None)
    erode = cv.erode(erode, None)
    erode = cv.erode(erode, None)
    # erode = cv.erode(erode, None)

    cv.imshow('erode', erode)

    # erode = ~erode

    contours, hierarchy = cv.findContours(erode, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    dst = cv.cvtColor(erode, cv.COLOR_GRAY2BGR)

    print(hierarchy)
    print('len(contours)', len(contours))
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
        ans.append(addnum)
        cv.drawContours(dst, contours, idx, (0, 0, 255), 2, cv.LINE_8, hierarchy)
        idx = hierarchy[0, idx, 0]

    ans.sort()
    print(ans)
    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

q2()

# cnt, labels, stats, centroids = cv.connectedComponentsWithStats(binarization)
# howmany = 0
# for i in range(1, cnt):
#     (x, y, w, h, area) = stats[i]
#     if area < 50:
#         continue
#     pt1 = (x, y)
#     pt2 = (x + w, y + h)
#     howmany += 1
#     cv.rectangle(dst, pt1, pt2, (0, 0, 255), 2)
#
# print('howmany: ', howmany)