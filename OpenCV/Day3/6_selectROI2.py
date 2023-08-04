import cv2

img = cv2.imread('./sun.jpg')

# selectROI: selectROI.py에서 했던 코드가 그냥 함수로 정의 되어있음 !
x, y, w, h = cv2.selectROI('img', img, False)

if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('roi', roi)

cv2.waitKey()