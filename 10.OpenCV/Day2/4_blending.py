# 같은 크기의 사진 두개를 찾아서 add연산 해보기
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./dolomites.jpg')
img2 = cv2.imread('./fireworks.jpg')

dst1 = img1 + img2
img_add = cv2.add(img1, img2)

img = {'img1': img1, 'img2': img2, 'dst1': dst1, 'img_add': img_add}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)

plt.show()