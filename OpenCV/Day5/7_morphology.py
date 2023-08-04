import cv2

img = cv2.imread('./circuit.bmp', cv2.IMREAD_GRAYSCALE)

# cv2.getStructuringElement(구조 요소의 모양, 사이즈)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
#침식
dst1 = cv2.erode(img, se)
#팽창 3*3(None)
dst2 = cv2.dilate(img, None)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1) # 침식
cv2.imshow('dst2', dst2) # 팽창
cv2.waitKey()

