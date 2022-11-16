import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import sys

img = cv2.imread(sys.argv[1],0) 

#cv2.imshow('original',img)


## Gamma Correction
def gammacorrection(img, gamma):              
    gam = np.empty((1,256), np.uint8)
    for i in range(256):
        gam[0,i] = pow(i/255,gamma)*255
    return cv2.LUT(img, gam)


## Contrast Enhancement
def contrastenhancement(img,x):
    new = np.zeros(img.shape, img.dtype)          
    for i in range(img.shape[0]):
                new[i] = np.clip(x*img[i], 0, 255)
    return new


img = gammacorrection(img, 0.4)
img = contrastenhancement(img,1.5)
img = cv2.equalizeHist(img)


# cv2.imshow('image',img)
# cv2.waitKey(0)

###############################

name = 'enhanced-' + sys.argv[1][2:]             ##OUTPUT IMAGE NAME = enhanced-cctvX.jpg
                                                                    ## where X=integer 

cv2.imwrite((name), img)
