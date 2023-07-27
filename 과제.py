import cv2
import numpy as np

#조윤재코드 참조했습니다!

# 이미지 불러오기
image = cv2.imread("namecard.jpg")
# ROI를 선택하고자 하는 이미지 복사해서 재표시
clone_image = image.copy()
cv2.imshow("Select ROI", image)

# 사다리꼴을 그리기 위한 점의 좌표를 리스트로 정의
points = []

def on_mouse(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(clone_image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select ROI", clone_image)

        # 4개의 점을 선택하면 사다리꼴 그리기
        if len(points) == 4:
            points_arr = np.array(points, np.int32)
            cv2.polylines(clone_image, [points_arr], isClosed=True, color=(0, 255, 0), thickness=2)
            cv2.imshow("Select ROI", clone_image)

            # 선택한 사다리꼴 내부를 마스킹하여 ROI 추출
            roi_mask = np.zeros(image.shape[:2], dtype=np.uint8)
            cv2.fillPoly(roi_mask, [points_arr], (255, 255, 255))
            roi = cv2.bitwise_and(image, image, mask=roi_mask)

            w, h = 550, 300
            dstQuad = np.array([[0,0], [w,0], [w,h], [0,h]], np.float32)
            srcQuad = np.array([[21, 445], [510, 211], [722, 405],[214, 748]], np.float32)

            if cv2.waitKey() == 13:
                pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
                dst = cv2.warpPerspective(roi, pers, (w, h))
                cv2.imshow('dst', dst)
                cv2.waitKey()


# 마우스 이벤트 콜백 함수 등록
cv2.setMouseCallback("Select ROI", on_mouse)
cv2.waitKey()