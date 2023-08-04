import cv2

img = cv2.imread('./sun.jpg')

x = 182
y = 15
w = 122
h = 120

roi = img[y: y+h, x:x+w]
# 해 복사해오기
img2 = roi.copy()
print(roi.shape)

# 해 두개 만들기
img[y:y+h, x+w:x+w+w] = roi

cv2.rectangle(img, (x, y), (x+w+w,  y+h), (0, 255, 0), 3)
cv2.imshow('img', img)
cv2.waitKey()