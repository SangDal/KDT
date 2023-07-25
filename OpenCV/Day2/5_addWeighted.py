import cv2
import numpy as np

img1 = cv2.imread('./dolomites.jpg')
img2 = cv2.imread('./fireworks.jpg')

alpha = 0.7

# 손으로 연산
dst1 = img1 * alpha + img2 * (1-alpha)
dst1 = dst1.astype(np.uint8)

# cv2.addWeighted 이용한 연산
dst2 = cv2.addWeighted(img1, alpha, img2,  (1-alpha), 0)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()


