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

	# threshold(param, thresh_val, fill_color, type)
	_, thresh = cv2.threshold(gray, 150, 225, cv2.THRESH_BINARY)


	# Find contours
	contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# filter out the small ones
	contours = [c for c in contours if cv2.contourArea(c) > 10000]

	# Display
	cv2.imshow('Normal',frame)
	cv2.imshow("Gray",gray)
	cv2.imshow("Thresh",thresh)

	for i in range(len(contours)):
		cv2.drawContours(frame, [contours[i]], 0, (0,255,0), 5)
	cv2.imshow("Contours", frame)

	if cv2.waitKey(50) == ord('q'):
		break


# release everything afterwards
cap.release()
cv2.destroyAllWindows()