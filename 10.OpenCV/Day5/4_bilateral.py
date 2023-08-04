import cv2

img = cv2.imread('./gaussian_noise.jpg', cv2.IMREAD_GRAYSCALE) # 소금-후추 잡음이 있는 원본
dst1 =cv2.GaussianBlur(img, (5, 5), 0)
dst = cv2.bilateralFilter(img, 5, 80, 80) # 바이레터럴 필터를 사용

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()