import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.arrowedLine(img, (0, 511), (511, 0), (0, 255, 0), 5)
cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)
cv2.circle(img, (256, 256), 100, (0, 0, 255), 2)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (255, 0, 0), 2)
pts = np.array([[100, 100], [200, 300], [400, 200], [300, 100]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 0), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (200, 300), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('Image', img)
cv2.imwrite('draw1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()