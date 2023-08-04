import cv2
import matplotlib.pyplot as plt


'''
# IMREAD_GRAYSCALE : 그레이스케일로 영상 불러오기
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img_gray', img_gray)

cv2.waitKey()
'''

'''
# 멧플랏으로 영상 띄우기 
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off') # 격자 없애달라
plt.imshow(img_gray, cmap='gray')
plt.show() # plt는 닫기 버튼을 누르면 됩니다. 
'''

'''
# RGB의 순서가 바뀌기 때문에 색이 조금 이상하다.
# Read할땐 rgb로 저장하고 보여줄땐  BGR로 출력하기 때문이다.
img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)# defult값이라서 IMREAD_COLOR는 생략이 가능함.
# BGR을 RGB로 변환
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
plt.axis('off') # 격자 없애달라
plt.imshow(img_rgb)

plt.show() # plt는 닫기 버튼을 누르면 됩니다.
'''

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)

img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.imshow(img_rgb)
plt.show()