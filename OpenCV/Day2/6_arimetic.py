# square.bmp (256 x 256)
# 같은 크기의 이미지 (이미지를 짤라도 된다) 와 연산해보기
# add, addWeighted, subtract, absdiff
# matplotlib의 subplot을 이용해서 이미지 비교 하기


# 같은 크기의 사진 두개를 찾아서 add연산 해보기
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./lion.png')
img2 = cv2.imread('./square.bmp')

alpha = 0.7

img_add = cv2.add(img1, img2)
img_weight = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
img_sub = cv2.subtract(img1, img2)
img_absd = cv2.absdiff(img1, img2)

img = {'img1': img1, 'img2': img2, 'img_add': img_add, 'img_addWeighted': img_weight, 'img_subtract': img_sub, 'img_absdiff': img_absd}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(3, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)

plt.show()