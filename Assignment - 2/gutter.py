import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import sys

#img = cv2.imread('gutters1.jpg') 
img = cv2.imread(sys.argv[1])

#cv2.imshow('original',img)
org=img

kernel =  np.ones((6,6), np.uint8)
img = cv2.dilate(img, kernel)                    #ignoring text in the image
shadow = cv2.GaussianBlur(img, (5,5), 1)         #finding pseudo image casting shadow
img = shadow - org
img = 255 - img

#cv2.imshow('cleaned',img)
#cv2.waitKey(0)

cv2.imwrite(('cleaned-gutter.jpg'), img)
