import cv2, os

def imagshow():
    lst = os.listdir("Screenshots")
    for i in lst:
        img=cv2.imread(".\\SC\\{}".format(i))
        cv2.imshow(i,img)
        key=cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    imagshow()
