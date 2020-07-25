# haarcascade_frontalface_default.xml
import cv2

img = cv2.imread("face5.jpg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cordiante = cascade.detectMultiScale(grey, 1.1, 20)
# print(face_cordiante)

for i in face_cordiante:
    # x=i[0]-20
    # y=i[1]-20
    # w=i[2]+40
    # h=i[3]+40
    # print(x,y,w,h)

    x=i[0]
    y=i[1]
    w=i[2]
    h=i[3]
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
    cv2.putText(img, "Person", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)

cv2.imshow("Detected Face", img)
cv2.waitKey(0)
cv2.destroyWindow(("Detected Face"))