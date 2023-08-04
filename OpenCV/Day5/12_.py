import cv2

img = cv2.imread('./hat.png')
# img = cv2.imread('./hand.jpg')

cpy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 이진화 한거고
_, thr = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 좌표값 뽑은거고
contour, _ =  cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contour[0])
cnt = contour[0]

cv2.drawContours(img, [cnt], -1, (255, 0, 0), 2)
check = cv2.isContourConvex(cnt)
print(check)

if check:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(cpy, [hull], -1, (0,255,0), 2)

cv2.imshow('contour', img)
cv2.waitKey()