# %%
import numpy as np
import cv2 as cv
import time
import math


# parameters for circle
x_y = 400
center_x_y = int(x_y/2)
radius = int(x_y/2.5)
radius_for_sec = int(radius/1.2)
radius_for_min = int(radius/1.6)
radius_for_hr = int(radius/2)
radius_for_Hr_lable = radius
diameter = int(radius*2)
count_of_dots = 0


# creat matrix for clock
image = np.ones((x_y,x_y),dtype=np.uint8)

while True:
    
    # Time implimentation radian values
    Count_60 = np.linspace(0,6.283,61)
    Count_12 = np.linspace(0,6.283,13)

    copy = image.copy()
    view = image.view()

    # dot addition on edges of clock
    for i in range(2):
        count_of_dots += 1
        if count_of_dots == 12:
            count_of_dots = 0
        dot_angle = Count_12[count_of_dots]
        x_d = int(radius_for_Hr_lable*np.cos(dot_angle)+center_x_y)
        y_d = int(radius_for_Hr_lable*np.sin(dot_angle)+center_x_y)

        if count_of_dots == 0 or count_of_dots == 3 or count_of_dots == 6 or count_of_dots == 9:
            cv.circle(view,(x_d,y_d),8,(255,255,255),-2)
        else:
            cv.circle(view,(x_d,y_d),4,(255,255,255),-2)


    # second
    sec = int(time.strftime("%S"))
    sec_angle = (Count_60[sec])

    # minuit
    minuit = int(time.strftime("%M"))
    min_angle = (Count_60[minuit])

    # hr
    hr = int(time.strftime("%I"))
    hr_angle = (Count_12[hr])


    # sec
    sec_coordinate_x = int(radius_for_sec*np.cos(sec_angle)+center_x_y)
    sec_coordinate_y = int(radius_for_sec*np.sin(sec_angle)+center_x_y)

    # min
    min_coordinate_x = int(radius_for_min*np.cos(min_angle)+center_x_y)
    min_coordinate_y = int(radius_for_min*np.sin(min_angle)+center_x_y)

    # hour
    hr_coordinate_x = int(radius_for_hr*np.cos(hr_angle)+center_x_y)
    hr_coordinate_y = int(radius_for_hr*np.sin(hr_angle)+center_x_y)


    # drawing
    cv.circle(image,(center_x_y,center_x_y),radius,(255,255,255),1)
    cv.circle(image,(center_x_y,center_x_y),10,(255,255,255),-1)
    
    cv.line(copy,(center_x_y,center_x_y),(sec_coordinate_x,sec_coordinate_y),(255,255,255),2)
    cv.line(copy,(center_x_y,center_x_y),(min_coordinate_x,min_coordinate_y),(255,255,255),2)
    cv.line(copy,(center_x_y,center_x_y),(hr_coordinate_x,hr_coordinate_y),(255,255,255),2)

    # rotate the clock to align with proper view
    rotated_90 = cv.rotate(copy,cv.ROTATE_90_COUNTERCLOCKWISE)


    
    # End loop
    if cv.waitKey(10) == ord("q"):
        break
    cv.imshow("img",rotated_90)

# descard 
cv.destroyAllWindows()