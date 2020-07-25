## capture.py
import cv2

counter = 0 
video_name = "video.mp4"
cap=cv2.VideoCapture(video_name) # object | cv2.VideoCapture(0) captures from the primary camera
if cap.isOpened() == False:
    print("Error Occured")
while cap.isOpened():
    check, img = cap.read()
    if check == True:
        cv2.imshow("Frame of video", img)
        cv2.waitKey(1) ## 1 millisecond
        counter+=1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(".\\images\\{}.jpg",format(counter), img)
    else:
        break

cap.release()
cv2.destroyWindow("Frame of video")