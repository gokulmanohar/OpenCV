# haarcascade_frontalface_default.xml
import cv2
import numpy
import os

file_list = os.listdir(".\players")
print(file_list)
for img_name in file_list:
    img = cv2.imread("players/"+img_name)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_cordiante = cascade.detectMultiScale(grey, minNeighbors=10)

    for i in face_cordiante:
        x = i[0]-20
        y = i[1]-20
        w = i[2]+40
        h = i[3]+40
        crop_img = img[y:y+h, x:x+w]

    img_name = img_name.split(".")[0]+"_crop.jpg"
    cv2.imwrite(img_name, crop_img)
    cv2.imshow("Detected Face", crop_img)
    cv2.waitKey(0)
    cv2.destroyWindow(("Detected Face"))