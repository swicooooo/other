from cv2 import cv2 

def get_pos(imageSrc):
    img=cv2.imread(imageSrc)
    
    cv2.imshow('image',img)
    cv2.waitKey()
    blurred=cv2.GaussianBlur(img,(5,5),0,0)
    canny=cv2.Canny(blurred,0,100)
    contours, hierarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours)) 

    for contour in contours:
        area=cv2.contourArea(contour)
        zhouchang=cv2.arcLength(contour,True)
        if 4225 <area< 7225 and 260 <zhouchang< 340:
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imwrite('1.jpg',img)
            return x
    return 0

def Video():
    capture=cv2.VideoCapture(0)
    while True:
        ret,frame=capture.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray',gray)
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    # print(get_pos('captche.png'))
    Video()
    

    
    