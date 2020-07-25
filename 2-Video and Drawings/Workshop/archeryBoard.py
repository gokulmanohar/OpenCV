import cv2
import numpy as np

img=np.full((500, 500, 3), 255, np.uint8) #creates a white background image
cv2.circle(img, (250,250), 250, (245, 135, 66), -1)
cv2.circle(img, (250,250), 200, (111, 219, 29), -1)
cv2.circle(img, (250,250), 150, (0, 219, 255), -1)
cv2.imshow("Archery Board", img)
cv2.waitKey(0)
cv2.destroyWindow(("Archery Board"))