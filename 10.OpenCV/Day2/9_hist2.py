# dog.bmp 이미지를 사용하여 3채널 RGB로 계산해 히스토그램 그리기
# 하나의 plot에서 RGB 그래프 그리기

import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./dog.bmp')

colors = ['b', 'g', 'r']
# b,g,r로 받으면 스칼라 값인데, bgr이렇게 한개의 변수로 받으면 리스트가 된다!
bgr = cv2.split(src)

for (b, c) in zip(bgr, colors):
    hist = cv2.calcHist([b], [0], None, [256], [0, 255])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
plt.show()
cv2.waitKey()