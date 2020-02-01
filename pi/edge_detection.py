import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('/Users/user/Pictures/rock.jpg',cv2.IMREAD_GRAYSCALE)

'''
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''





image = cv2.imread('/Users/user/Pictures/watch.jpeg')
watch_image = np.copy(image)
gray = cv2.cvtColor(watch_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,  5), 0)
canny = cv2.Canny(blur, 50, 150)
cv2.imshow("result", canny)
cv2.waitKey(0)
