import numpy as np
import cv2

#cap=cv2.VideoCapture(0)

#while True:

#    ret, frame = cap.read()

#    cv2.imshow('frame',frame)
#    if cv2.waitKey(1)==ord("q"):
#        break

#cap.release()
#cv2.destroyAllWindows()





lower_green=np.array([36,0,0])
upper_green=np.array([86,255,255])
lower_yellow=np.array([20, 100, 100])
upper_yellow=np.array([30, 255, 255])
lower_red = np.array([0,100,20])
upper_red = np.array([10,255,255])
lower_data=[lower_green,lower_yellow,lower_red]
upper_data=[upper_green,upper_yellow,upper_red]

for i in range(3):
    image = cv2.imread(r"C:\Users\rouic\Desktop\green.jpg")
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower=lower_data[i]
    upper=upper_data[i]
    mask=cv2.inRange(hsv,lower,upper)
    result= cv2.bitwise_and(image,image,mask=mask)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    count = cv2.countNonZero(gray)
    total=image.shape[0]*image.shape[1]
    print(count)
    print(total)
    print(count/total)
    if(count/total>0.03):
        if(i==0):
            print('ÂÌÂë')
        elif (i==1):
            print('»ÆÂë')
        else:
            print('ºìÂë')
        
    #cv2.imshow('hsv',gray)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


