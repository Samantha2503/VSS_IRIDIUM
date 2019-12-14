import cv2
import numpy as np
import math

lower_red = np.array([0,102,148])
upper_red = np.array([179,230,255])

lower_blue = np.array([97,90,59])
upper_blue = np.array([235,209,239])


cap= cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur= cv2.GaussianBlur(frame,(7,7),0)
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    union= cv2.inRange(hsv, lower_blue, upper_blue)
    
    c=0
    s=0

  
    f1= cv2.erode(union, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    f2= cv2.erode(f1, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    object= cv2.moments(f2)
    
    if object['m00'] > 50000:
        c= 1
        xblue= int(object['m10']/object['m00'])
        yblue= int(object['m01']/object['m00'])
        cv2.circle(frame, (xblue,yblue), 10, (0,255,0), 2)
        print(xblue,yblue)
    
    union= cv2.inRange(hsv, lower_red, upper_red)

    f3= cv2.erode(union, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    f4= cv2.erode(f3, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    object= cv2.moments(f4)

    
    if object['m00'] > 50000:
        s= 1
        xred= int(object['m10']/object['m00'])
        yred= int(object['m01']/object['m00'])
        cv2.circle(frame, (xred,yred), 10, (0,255,0), 2)
        print(xred,yred)
    
    if s==1 and c==1:

        d= math.sqrt(math.pow(xred-xblue,2)+math.pow(yred-yblue,2))
        print(d)


        r= abs(xred-xblue)
        b= abs(yred- yblue)

        a= math.atan2(b,r)
        angle= a * 180/math.pi
        print("angle", angle)

    cv2.imshow('rgb',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()