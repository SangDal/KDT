import cv2
import pytesseract
import numpy as np

# 좌표를 sort해줄 함수
def reroderPts(pts):
    # lexsort(): 배열의 차원을 기준으로 정렬하는 기능
    # 정렬하려는 배열의 키 또는 튜플.
    idx = np.lexsort((pts[:,1], pts[:, 0]))
    pts = pts[idx]


    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]
    if pts[2, 1] > pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    print(pts)
    return pts

src = cv2.imread('./namecard.jpg')

# 읽어드려올 사이즈 설정하기
dw, dh = 700, 400
srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
dst = np.zeros((dh, dw), np.uint8)

# 이진화 하기 위해서 그레이로 바꾸기
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 따기
countours, _ =  cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cpy = src.copy()
for pts in countours:
    if cv2.contourArea(pts) < 1000:
        continue
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    # print(approx)
    '''
    프린트 결과 
    [[[903 199]]
    
     [[179 200]]
    
     [[159 593]]
    
     [[938 581]]]
    '''
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue

    # 라인따기
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2)
    # print(approx.reshape(4, 2).astype(np.float32))

    srcQuad = reroderPts(approx.reshape(4, 2).astype(np.float32))

cv2.imshow('src', src)
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw,dh))
dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(dst_gray, lang='kor+eng'))
cv2.imshow('dst', dst)
cv2.waitKey()