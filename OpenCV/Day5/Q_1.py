import cv2

MODES = ["Normal", "Gaussian", "Canny"]


def apply_gaussian_filter(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)


def apply_canny_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)


if __name__ == "__main__":
    cap = cv2.VideoCapture('./158980.mp4')
    current_mode = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):

            # 스페이스바를 누를 때마다 다음 모드로 변경
            current_mode = (current_mode + 1) % len(MODES)

        if current_mode == 1:
            filtered_frame = apply_gaussian_filter(frame)

        elif current_mode == 2:
            filtered_frame = apply_canny_filter(frame)
        else:
            filtered_frame = frame

        cv2.imshow(f'Filtered Webcam - {MODES[current_mode]}', filtered_frame)

        if key == 27:  # ESC 키를 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()
