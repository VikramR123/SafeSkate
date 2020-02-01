import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG() # bg mask
# fgmask = fgbg.apply(frame) # apply mask
# cv2.imshow('With Bg Reduction',fgmask) # show mask

while True:
	# Read by frame
	_, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	flag, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY) # flag is useless


	# Find contours
	contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contours = sorted(contours, key=cv2.contourArea,reverse=True)
	# Select long perimeters only
	perimeters = [cv2.arcLength(contours[i],True) for i in range(len(contours))]
	listindex=[i for i in range(15) if perimeters[i]>perimeters[0]/2]
	numcards=len(listindex)

	# Display
	cv2.imshow('Normal',frame)
	cv2.imshow("Gray",gray)
	cv2.imshow("Thresh",thresh)

	copy = frame.copy()
	[cv2.drawContours(copy, [contours[i]], 0, (0,255,0), 5) for i in listindex]
	cv2.imshow("Contours", copy)
	


	if cv2.waitKey(50) == ord('q'):
		break


# release everything afterwards
cap.release()
cv2.destroyAllWindows()