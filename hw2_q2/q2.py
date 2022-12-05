import cv2 as cv

def q2():
    src = cv.imread('./diceAll.jpg', cv.IMREAD_GRAYSCALE)
    if src is None:
        print('Image load failed!')
        return

    _, threshold = cv.threshold(src, 128, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(threshold, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    dst = cv.cvtColor(threshold, cv.COLOR_GRAY2BGR)

    idx = 0
    cnt = 1
    ans = []

    while idx >= 0:
        addnum = 0
        while cnt < len(contours):
            if hierarchy[0, cnt, 2] < 0:
                addnum += 1
                cnt += 1
                continue
            cnt += 1
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