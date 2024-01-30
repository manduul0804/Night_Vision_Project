import cv2

import numpy as np
window_name = "Night_vision"
cap = cv2.VideoCapture(0)

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    ret, frame = cap.read()
    # frame = imutils.resize(frame, width=1280)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # frame = cv2.resize(frame, (540, 380), fx=0, fy=0,
    #                    interpolation = cv2.INTER_CUBIC)

    # cv2.imshow(window_name, frame)

    gaussianblur = cv2.GaussianBlur(frame, (5,5), 0)
    gray = cv2.cvtColor(gaussianblur, cv2.COLOR_BGR2GRAY)
    cv2.imshow(window_name, gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()