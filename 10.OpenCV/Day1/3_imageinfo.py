import cv2

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img_gray type:', type(img_gray)) # img_gray type: <class 'numpy.ndarray'>
print('img_gray shape:', img_gray.shape) # img_gray shape: (364, 548) => ((h(세로), w(가로))형태로 되어있다.)
print('img_gray dtype:', img_gray.dtype) # img_gray dtype: uint8

img_color = cv2.imread('./dog.bmp')
print('img_color type:', type(img_color)) # img_color type: <class 'numpy.ndarray'>
print('img_color shape:', img_color.shape) # img_color shape: (364, 548, 3) => ((h(세로), w(가로), 3)형태로 되어있다.)
print('img_color dtype:', img_color.dtype) # img_color dtype: uint8


# (img_color의 가로 * 세로) 형태로 출력하고 싶을땐!

height, width = img_color.shape[:2]
print(f'img_color 사이즈: {height} * {width}')

# 그레이스케일 영상과 컬러 영상을 구별하는 코드는?
if len(img_gray.shape) == 2:
    print('img_gray는 그레이스케일 영상입니다.')
elif len(img_gray.shape) == 3:
    print('img_gray는 컬러 영상입니다.')

# img_color에 특정 색 정보로 영상 출력
# BGR정보: (255, 102, 255)
# 강아지가 안보이게 위에 BGR색상으로 변경해보기
'''
# for문 이용하기
for x in range(h):
    for y in range(w):
        img_color[x, y] = (255, 102, 255)
cv2.imshow('img_color', img_color)
cv2.waitKey()
'''

# 파이썬의 기능 이용하기 좋은방법
img_color[:,:] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()

