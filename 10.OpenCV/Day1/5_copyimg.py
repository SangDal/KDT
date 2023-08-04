import cv2

img_origin = cv2.imread('./dog.bmp')

'''
# 메모리가 공유하고 있기때문에 원본을 건들면 copy도 변화된다. 
img_origin = img_origin[91:210, 125:245] # 범위 선택해서 짜르기 
img_copy = img_origin
'''

# .copy()를 이용해야 메모리 공유가 아닌 진짜 복사 된다!
img_copy = img_origin[91:210, 125:245].copy()

cv2.imshow('img_origin',img_origin)
cv2.imshow('img_copy',img_copy)
cv2.waitKey()