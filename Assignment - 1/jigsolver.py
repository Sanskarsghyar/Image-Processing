import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img = cv2.imread(sys.argv[1])       
#img = cv2.imread('jigsaw.jpg')           ## 797p X 421p
#cv2.imshow("input",img)

width,height = 190,200
pt1 = np.float32([[0,0],[0,200],[190,0],[190,200]])
pt2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
part1 = cv2.warpPerspective(img,matrix,(width,height))

#cv2.imshow("part",part1)

part1 = part1[:, :, [1,0,2]]               #### bgr to gbr


width,height = 190,209
pt1 = np.float32([[0,200],[0,409],[190,200],[190,409]])
pt2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
part2 = cv2.warpPerspective(img,matrix,(width,height))

part2 = cv2.flip(part2,0)                         ### upside down flip


width,height = 185,180
pt1 = np.float32([[515,150],[515,330],[700,150],[700,330]])
pt2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
part3 = cv2.warpPerspective(img,matrix,(width,height))

part3 = cv2.flip(part3,1)                          ##sidewise flip


width,height = 427,51
pt1 = np.float32([[370,370],[370,421],[797,370],[797,421]])
pt2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
part4 = cv2.warpPerspective(img,matrix,(width,height))

part4 = cv2.flip(part4,0)                         ### upside down flip


#########################################################

img[0: 209, 0:190] = part2
img[199:399, 0:190] = part1

#########################################################
img[150:330, 515:700] = part3
img[370:421, 370:797] = part4
#img1=img
#img1[201:400, 0:195] = part1

#img[399:405, 0:190] = np.pad(img[393:399, 0:190])

#cv2.imshow("part1",part1)
#cv2.imshow("part2",part2)
#cv2.imshow("part3",part3)
#cv2.imshow("part4",part4)
#cv2.imshow("output",img)
#cv2.waitKey(0)

cv2.imwrite(('jigsolved.jpg'), img)


#print(sys.argv[1])