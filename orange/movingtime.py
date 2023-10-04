import cv2
import numpy as np
import datetime

img = np.zeros((512, 512, 3), np.uint8)
frame = img.copy()
show_date = False
date_time = ""
def mouse_callback(event, x, y, flags, param):
    global date_time, frame, show_date, img
    if event == cv2.EVENT_LBUTTONDOWN:
        show_date = True
        now = datetime.datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, date_time, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', frame)
    elif event == cv2.EVENT_RBUTTONDOWN:
        show_date = False
        frame = img.copy()
        cv2.imshow('image', frame)
    elif event == cv2.EVENT_MOUSEMOVE:
        if show_date:
            frame = img.copy()
            now = datetime.datetime.now()
            date_time = now.strftime("%d-%m-%Y %H:%M:%S")
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, date_time, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('image', frame)

cv2.namedWindow('image', cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow('image', 512, 512)
cv2.setMouseCallback('image', mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()