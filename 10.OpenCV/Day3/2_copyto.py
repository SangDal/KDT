import cv2

src = cv2.imread('./airplane.bmp')
mask = cv2.imread('./mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('./field.bmp')

# 출력영상을 넣지 않으면 새로 영상을 만들어 낸다.
# 중요! 입력 영상과 마스크, 출력영상의 크기가 모두 같아야 합니다!
cv2.copyTo(src, mask, dst)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()