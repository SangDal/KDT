import cv2

img = cv2.imread('./dog.bmp')
cp = (img.shape[1] / 2, img.shape[0] /2)

#cv2.getRotationMatrix2D(중심좌표, 회전각도, 확대비율)
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)
dst = cv2.warpAffine(img, rot, (0, 0))

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey()