import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img = cv2.imread(sys.argv[1])
# img = cv2.imread('noisy1.jpg')
org=img
#cv2.imshow("input",img)

if sys.argv[1]=='./noisy1.jpg':
    img = cv2.bilateralFilter(img, 30, 60, 60)
    img = cv2.bilateralFilter(img, 50, 20, 20)
    #cv2.imshow("img",img)

else:
    img = cv2.bilateralFilter(img, 25, 60, 60)
    # cv2.imshow("img",img)
    # med = cv2.medianBlur(img, 3)
    # cv2.imshow("med",med)

# med = cv2.medianBlur(img, 9)
# cv2.imshow("med",med)

# gaus = cv2.GaussianBlur(img, (9,9),0)
# cv2.imshow("gaus",gaus)

dencol = cv2.fastNlMeansDenoisingColored(img, None, 8, 8, 5, 10)


# cv2.imshow("output",dencol)

# cv2.waitKey(0)

cv2.imwrite(('denoised.jpg'), img)


#print(sys.argv[1])