import cv2
import numpy as np

img=np.zeros((500,500, 3), np.uint8)
cv2.rectangle(img, (0,0), (500,500), (0,255,255), -1) #creates a Yellow rectangle background
cv2.putText(img, "OPENCV", (25,250), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3.5, (0,0,0), 4)
cv2.imshow("BlackinYellow", img)
cv2.waitKey(0)
cv2.destroyWindow(("BlackinYellow"))
