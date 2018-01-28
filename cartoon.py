import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    bi = cv2.bilateralFilter(frame,d=11,sigmaColor=9,sigmaSpace=7)  #bilateral filter
    img_gray = cv2.cvtColor(bi, cv2.COLOR_RGB2GRAY) #gray aaki
    img_blur = cv2.medianBlur(img_gray, 7)  #blur filter
    # detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=7,C=4)
    # convert back to color, bit-AND with color image
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_cartoon = cv2.bitwise_and(frame, img_edge)
 
    # display
    cv2.imshow("cartoon", img_cartoon)
    cv2.imshow('Original',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
