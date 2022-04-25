import numpy as np
import cv2



lower_green=np.array([36,0,0])
upper_green=np.array([86,255,255])
lower_yellow=np.array([20, 100, 100])
upper_yellow=np.array([30, 255, 255])
lower_red = np.array([0,100,20])
upper_red = np.array([10,255,255])
lower_data=[lower_green,lower_yellow,lower_red]
upper_data=[upper_green,upper_yellow,upper_red]
color_name_list=["绿码","黄码","红码"]
color_percent=-1
color_name=""
image = cv2.imread(r"C:\Users\rouic\Desktop\yellow.jpg")
for i in range(3):
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower=lower_data[i]
    upper=upper_data[i]
    mask=cv2.inRange(hsv,lower,upper)
    #result= cv2.bitwise_and(image,image,mask=mask)
    #gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    count = cv2.countNonZero(mask)
    total=image.shape[0]*image.shape[1]
    if color_percent<count/total:
        color_percent=count/total
        color_name=color_name_list[i]
        
    #cv2.imshow('hsv',mask)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


print(color_name)