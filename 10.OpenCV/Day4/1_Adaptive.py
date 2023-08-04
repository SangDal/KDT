import cv2
import matplotlib.pyplot as plt

block_size = 9

img = cv2.imread('./sudoku.jpg', cv2.IMREAD_GRAYSCALE)

th, dst1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.adaptiveThreshold(영상, 임계값을 만족하는 픽셀에 적용할 값, 임계값 결정 방법, Threshold 적용방법, 블록사이즈, 가감할 상수)

# ADAPTIVE_THRESH_MEAN_C
dst2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, 5)
# ADAPTIVE_THRESH_GAUSSIAN_C
dst3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, 5)


dic = {'img' : img, 'dst1':dst1, 'dst2' : dst2,'dst3':dst3}

for i, (k,v) in enumerate(dic.items()):

    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,'gray')

plt.show()