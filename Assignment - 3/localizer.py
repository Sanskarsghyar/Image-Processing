import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img = cv2.imread(sys.argv[1])
# cv2.imshow("inpu",img)

# print(img.shape) 

x,y=0,0
b,g,r = 0,0,0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b,g,r = img[i,j,0],img[i,j,1],img[i,j,2]

r = np.mean(img[:,:,2])
g = np.mean(img[:,:,1])
b = np.mean(img[:,:,0])

x = abs(np.mean(img[:,:,1])-np.mean(img[:,:,0]))
y = abs(2*np.mean(img[:,:,1])-np.mean(img[:,:,2])-np.mean(img[:,:,0]))

# print(abs(np.mean(img[:,:,1]) - np.mean(img[:,:,0])))
# print(abs(2*np.mean(img[:,:,1]) - np.mean(img[:,:,2]) - np.mean(img[:,:,0])))

#Grass
if( (0<=x and x<=80) and (12<=y and y<=85) ):
    print(2)

#Road
elif( (6<x and x<=20) and (0<=y and y<=12) ):
    print(3)

#Building
else:
    print(1)

# # r0 = np.mean(img[:,:,2])
# # g0 = np.mean(img[:,:,1])
# # b0 = np.mean(img[:,:,0])

# print(abs(np.mean(img[:,:,1]) - np.mean(img[:,:,0])))
# print(abs(2*np.mean(img[:,:,1]) - np.mean(img[:,:,2]) - np.mean(img[:,:,0])))

# print(abs(np.mean(img[:,:,1] - img[:,:,0])))
# print(abs(np.mean(2*img[:,:,1] - img[:,:,0] - img[:,:,2])))



# src=img
# src[:,:,0] = np.zeros([img.shape[0], img.shape[1]])
# src[:,:,2] = np.zeros([img.shape[0], img.shape[1]])

# im = img[:,:,1]
# cv2.imshow("input",src)


# cv2.imshow("output",img)

# cv2.waitKey(0)

#print(ans)