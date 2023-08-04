import cv2

img = cv2.imread('./dog.bmp')
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey()
    if keyvalue == ord('i') or keyvalue == ord('I'): #ord(): 아스키코드 값
        img = ~img      # ~ : 반전시킴
        cv2.imshow('image', img)
    elif keyvalue == 27:
        break