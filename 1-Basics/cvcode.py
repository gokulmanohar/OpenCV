import cv2
def main():
    img=cv2.imread("black.jpg",0)
    # print(img.size)
    print(img.shape)
    # cv2.imwrite(".\\images\\created.jpg",img)


if __name__=="__main__":
    main()


"""
img=cv2.imread("black.jpg",0) #greyscale image -  read 0
cv2.imwrite(".\\images\\created.jpg",img)
img.shape
img.size
cv2.imshow("Parrot", img)
cv2.waitKey(0) #button press: 0 #<timeinmillisecond>
cv2.distroyWindow("Parrot")


"""