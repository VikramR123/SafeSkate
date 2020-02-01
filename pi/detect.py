import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	# Read by frame
	ret, frame = cap.read()

	# Display the frame
	cv2.imshow('frame',frame)

	if cv2.waitKey(50) & 0xFF == ord('q'):
		break


# release everything afterwards
cap.release()
cv2.destroyAllWindows()