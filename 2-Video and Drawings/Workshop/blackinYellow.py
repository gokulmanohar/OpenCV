import cv2
import numpy as np

img=np.zeros((500,500, 3), np.uint8)
cv2.rectangle(img, (0,0), (500,500), (0,255,255), -1)
cv2.imshow("Archery Board", img)
cv2.waitKey(0)
cv2.destroyWindow(("Archery Board"))
