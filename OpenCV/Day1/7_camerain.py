import sys
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exit()

print('카메라 연결 성공!')
print('가로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27: # 27: ESC키를 뜻함
        break

cap.release() # 릴리즈 해주면 메모리에서 날려주기때문에 메모리를 아낄수 있다.