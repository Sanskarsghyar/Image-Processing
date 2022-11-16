import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

y = cv2.imread(sys.argv[1])
# img = cv2.imread('Y.jpg')
# cv2.imshow("y2",y)

cb = cv2.imread(sys.argv[2])
# img = cv2.imread('Cb4.jpg')
cb = cv2.resize(cb,(960,622))      ## Upscaling cb from 240*156 to 960*622
# cv2.imshow("cb4",cb)

cr = cv2.imread(sys.argv[3])
# img = cv2.imread('Cr4.jpg')
cr = cv2.resize(cr,(960,622))      ## Upscaling cr from 240*156 to 960*622
# cv2.imshow("cr4",cr)

### Initialising img with 1st channel as Y, 2nd channel as Cr, 3rd channel as Cb
img = np.empty((622,960,3))
img[:,:,0] = y[:,:,0]          ## Making 1st channel of img as Y
img[:,:,1] = cr[:,:,0]         ## Making 2nd channel of img as Cr
img[:,:,2] = cb[:,:,0]         ## Making 3rd channel of img as Cb


RGB = np.empty((622,960,3))

y   = img[:,:,0]
cb  = img[:,:,1] - 128
cr  = img[:,:,2] - 128

#### This transformation of YCbCr to RGB is taken from Wikipedia
RGB[:,:,0] = y + 1.402 * cr                    ## R Channel
RGB[:,:,1] = y - 0.34414 * cb - 0.71414 * cr   ## G Channel
RGB[:,:,2] = y + 1.772 * cb                    ## B Channel

RGB[RGB<0] = 0         # If pixel value < 0, then make it 0
RGB[RGB>255] = 255     # If pixel value > 255, then make it 255

RGB = np.uint8(RGB)


# cv2.imshow("output",img)

######## Direct cv2 function for Ycbcr to RGB
# cv2.imshow("outputcv",cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR))

cv2.imwrite(('flyingelephant.jpg'), RGB)


# cv2.waitKey(0)
