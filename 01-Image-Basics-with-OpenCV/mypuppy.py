import cv2

img = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)

while True:
  cv2.imshow("Puppy", img)
  # If waited at least 1ms and pressed Esc key
  if cv2.waitKey(1) & 0xFF == 27:
    break

cv2.destroyAllWindows()