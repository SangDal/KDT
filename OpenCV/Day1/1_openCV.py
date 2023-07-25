# Open CV 임포트
import cv2

# 코드실행 단축키 : 컨트롤 + 쉬프트 + F10
print('현재 opencv의 버전:', cv2.__version__)

# 옵션을 주지 않으면 컬러 영상으로 읽어온다.
# 영상을 가져올때 BGR순서(Blue-> green-> Red)로 가지고 띄운다!
img = cv2.imread('./dog.bmp') # cv2.IMREAD_GRAYSCALE: 그레이스케일로 읽어오는 옵션
cv2.imshow('img', img) # ('창이름', 영상객체)
cv2.waitKey() # 키보드에 아무키를 누르기 전까지 화면이 꺼지지 않는다.

