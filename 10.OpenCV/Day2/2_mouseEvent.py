import cv2
import numpy as np

# 전역변수 x,y 마우스 좌표를 저장해주고 싶어서 만듦
oldx = oldy = 0

def on_mouse(event, x, y, flags, param):
    global  oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x,y # 콜백함수 이기때문에 좌표값(x,y)가 oldx,oldy에 저장된다.
        print('왼쪽 버튼이 눌렸습니다: %d, %d' % (x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼이 때졌어요: %d, %d' % (x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
            oldx, oldy = x, y



# 스케치북 (500(px),500(px), 3(컬러)) 라는뜻 500X500짜리 컬러 스케치북을 만들겠다.
img = np.ones((500, 500, 3), dtype=np.uint8) * 255
# 창이름 만들기
# 원래는 그냥 'img'라고 해도 창이름이 셋팅 되지만, 이벤트를 발생시킬때는 창이름을 만들어주는것이 좋다.
cv2.namedWindow('img')

# ('img'(창이름), on_mouse(콜백함수), img(파라미터))
cv2.setMouseCallback('img', on_mouse, img)

cv2.imshow('img', img)
cv2.waitKey()
