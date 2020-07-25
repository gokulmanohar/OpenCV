import cv2
import numpy as np


"""
Change dimension
    - only to a small size
"""
def changeDimension(): #Change dimensions - only to a small size
    img=cv2.imread("logo.jpg")
    resizeimg=cv2.resize(img, (100,100))
    cv2.imwrite("SmallImage.jpg", resizeimg)

def blackImage():
    img=np.zeros((720, 720, 3), np.uint8)
    cv2.imshow("BlackImage", img)
    cv2.waitKey(0)
    cv2.destroyWindow(("BlackImage"))
    cv2.imwrite("BlackImage.jpg", img)

def drawLineinImage():
    img=np.zeros((520, 520, 3), np.uint8)
    cv2.line(img, (0,0), (515,515), (0,235,0), 3) #BGR format, (0,0) topleft
    cv2.imshow("LineBlackImage", img)
    cv2.waitKey(0)
    cv2.destroyWindow(("LineBlackImage"))
    
def drawRectinImage():
    img=np.zeros((520, 520, 3), np.uint8)
    cv2.rectangle(img, (150,150), (450,450), (210,235,0), -1) #BGR format | (0,0)  topleft | -1 colourfill
    cv2.imshow("RectangleBlackImage", img)
    cv2.waitKey(0)
    cv2.destroyWindow(("RectangleBlackImage"))

def drawCircleinImage():
    img=np.zeros((520, 520, 3), np.uint8)
    cv2.circle(img, (150,150), 50, (210,235,0), 3) #BGR format | (0,0)  topleft | -1 colourfill
    cv2.imshow("CircleBlackImage", img)
    cv2.waitKey(0)
    cv2.destroyWindow(("CircleBlackImage"))

def TextinImage():
    img=np.zeros((520, 520, 3), np.uint8)
    cv2.putText(img, "Peter", (200,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
    cv2.imshow("TextinImage", img)
    cv2.waitKey(0)
    cv2.destroyWindow(("TextinImage"))

if __name__=="__main__":
    # changeDimension()
    # blackImage()
    # drawLineinImage()
    # drawRectinImage()
    # drawCircleinImage()
    TextinImage()
    
