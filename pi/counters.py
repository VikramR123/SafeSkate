import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import math


# Black and White
'''
image = cv2.imread('/Users/user/Pictures/watch.jpeg')

watch_image = np.copy(image)
gray = cv2.cvtColor(watch_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,  5), 0)
canny = cv2.Canny(blur, 50, 150)
cv2.imshow("result", canny)
cv2.waitKey(0)
'''



# Contouring
# Prepocess

img = cv2.imread('/Users/user/Documents/bottle1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("TEST", img)



gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(1,1),1000)
flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)
# Find contours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea,reverse=True) 
# Select long perimeters only
perimeters = [cv2.arcLength(contours[i],True) for i in range(len(contours))]
listindex=[i for i in range(15) if perimeters[i]>perimeters[0]/2]
numcards=len(listindex)
# Show image
imgcont = img.copy()
[cv2.drawContours(imgcont, [contours[i]], 0, (0,255,0), 5) for i in listindex]
cv2.imshow("testing", imgcont)



