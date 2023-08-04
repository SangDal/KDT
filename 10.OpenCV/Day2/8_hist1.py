import cv2
import matplotlib.pyplot as plt

src = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
#  cv2.calcHist([영상], [히스토그램을 구할 채널], None, [빈의 개수를 나타내는 리스트], [히스토그램 각 차원의 최소값과 최대값으로 구성된 리스트])
hist = cv2.calcHist([src], [0], None, [256], [0, 255])
cv2.imshow('src', src)
plt.plot(hist)
plt.show()
cv2.waitKey()