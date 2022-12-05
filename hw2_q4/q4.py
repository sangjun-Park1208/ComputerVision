import cv2 as cv

def q4():
    src = cv.imread('./img4_8.png', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    # 양방향 필터
    filtered = cv.bilateralFilter(src, -1, 15, 15)
    cv.imshow('filtered', filtered)

    # 샤프닝
    blurred = cv.GaussianBlur(filtered, (0, 0), 4, 4)
    alpha = 1.0
    sharped = cv.addWeighted(filtered, 1 + alpha, blurred, -alpha, 0.0)
    sharped = cv.addWeighted(sharped, 1 + alpha, blurred, -alpha, 0.0)
    sharped = cv.addWeighted(sharped, 1 + alpha, blurred, -alpha, 0.0)
    cv.imshow('sharped', sharped)

    # 적응형 이진화
    binarization = cv.adaptiveThreshold(sharped, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 16)
    cv.imshow('binarization', binarization)

    # 침식
    erode = cv.erode(binarization, None)
    cv.imshow('erode', erode)


    contours, hierarchy = cv.findContours(erode, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    dst = cv.cvtColor(erode, cv.COLOR_GRAY2BGR)

    idx = 0
    i = 1
    ans = []

    cnt = 0
    while idx >= 0:
        addnum = 0
        while i < len(contours):
            if cv.contourArea(contours[i]) < 650:
                i += 1
                continue
            cnt += 1
            if hierarchy[0, i, 2] < 0: # 자식이 없는 경우
                addnum += 1
                i += 1
                continue
            i += 1
            break

        cv.drawContours(dst, contours, idx, (0, 0, 255), 1, cv.LINE_8, hierarchy)
        idx = hierarchy[0, idx, 0]
        if addnum == 0:
            continue
        ans.append(addnum)

    ans.sort()
    ans.remove(len(ans)-1) # 마지막 인덱스는 배경 전체에 대한 객체
    print(ans)
    cv.imshow('src', src)
    cv.imshow('dst', dst)
    cv.waitKey()
    cv.destroyAllWindows()

q4()