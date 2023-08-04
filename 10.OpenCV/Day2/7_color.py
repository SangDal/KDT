import cv2

# BGRA도 가능하다!
#src1 = cv2.imread('./candies.png', cv2.IMREAD_UNCHANGED) # 알파채널(투명도) 포함
src = cv2.imread('./candies.png')
print('shape:', src.shape)
print('dtype:', src.dtype)

'''
b= src[:, :, 0]
g= src[:, :, 1]
r= src[:, :, 2]
'''

# 위내용을 함수 이용하기
b, g, r = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()