import numpy as np
import cv2
import sys

#N=int(input())
N=int(sys.argv[1])                             ##take input as int

firstdigit = int(N/10)
lastdigit = N%10

img = np.zeros((300, 500), dtype=np.uint8) ##size of output image (window)

r = 25                                     ##radius

pattern = {}                               ##positions of dots
pattern[0] = [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]              ## 5 rows & 3 columns
pattern[1] = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
pattern[2] = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
pattern[3] = [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]
pattern[4] = [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]
pattern[5] = [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]
pattern[6] = [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]
pattern[7] = [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
pattern[8] = [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
pattern[9] = [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]

l = 40

for i in range(2):
    if(i==0): dig = pattern[firstdigit]
    else: dig = pattern[lastdigit]
    for i in range(5):                               ## row
        for j in range(3):                           ##column
            if dig[i][j]:
                x = l + 5 + 10*j + r + 2*r*j                    ## x coord of centre
                y = 5 + 10*i + r + 2*r*i                        ## y coord of centre
                centre = (x,y)                                  ## centre of circle
                img = cv2.circle(img, centre , r, 255, -1)
    l += 200 + 40

#cv2.imshow("im",img)
#cv2.waitKey(0)
cv2.imwrite(('dotmatrix.jpg'), img)
