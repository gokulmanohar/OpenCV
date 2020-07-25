import cv2
import numpy as np

img=np.full((500, 500, 3), 255, np.uint8) # creates a white background image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyWindow(("Image"))