import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import sys

img = cv2.imread(sys.argv[1]) 

#cv2.imshow('img',img)

org = img

########################################
img = cv2.Canny(img,100,375)
img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

#Making colour of detected edges as blue colour
img[np.where((img==[255, 255, 255]).all(axis=2))] = [255, 0, 0]
org = cv2.addWeighted(org,1,img,1,0)           ##combine
########################################

# ****** Using Hough diffrent images needs different threshold and other parameters, hence I don't used it here********

# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img = cv2.Canny(img,100,360)
# lines_list =[]
# lines = cv2.HoughLinesP(img, 8, (np.pi)/180, threshold=8, minLineLength=80, maxLineGap=15)
# for points in lines:
#     x1,y1,x2,y2=points[0]
#     cv2.line(org,(x1,y1),(x2,y2),(0,0,255),1)
#     lines_list.append([(x1,y1),(x2,y2)])


# cv2.imshow('edge',org)
# cv2.waitKey(0)

###############################

name = 'robolin-' + sys.argv[1][2:]           ##OUTPUT IMAGE NAME = robolin-tilesX.jpg
                                                               ## where X=integer 
cv2.imwrite((name), org)
