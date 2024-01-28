import cv2


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame',frame)