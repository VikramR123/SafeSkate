import cv2
import numpy as np
from firebase import firebase


fb = firebase.FirebaseApplication("https://safeskate-499c0.firebaseio.com/", None)

cap = cv2.VideoCapture(0)
# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG() # bg mask
# fgmask = fgbg.apply(frame) # apply mask
# cv2.imshow('With Bg Reduction',fgmask) # show mask
j = 0

while True:
	# Read by frame
	_, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	# threshold(param, thresh_val, fill_color, type)
	_, thresh = cv2.threshold(gray, 100, 225, cv2.THRESH_BINARY)


	# Find contours
	contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# filter out the small ones
	contours = [c for c in contours if cv2.contourArea(c) > 10000]
	if(contours):
		print("Collision detected: ",j)
		j += 1
		fb.put('/safeskate-499c0/obs_table', 'obstruction', 1)
	else:
		fb.put('/safeskate-499c0/obs_table', 'obstruction', 0)

	# Display
	cv2.imshow('Normal',frame)
	cv2.imshow("Thresh",thresh)

	for i in range(len(contours)):
		cv2.drawContours(frame, [contours[i]], 0, (0,255,0), 5)
	cv2.imshow("Contours", frame)

	if cv2.waitKey(50) == ord('q'):
		break


fb.put('/safeskate-499c0/obs_table', 'obstruction', 0)
# release everything afterwards
cap.release()
cv2.destroyAllWindows()
