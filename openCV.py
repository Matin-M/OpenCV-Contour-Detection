import cv2
import numpy as np
#import matplotlib.pyplot as cv2

 
def function(param):
	pass

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("dots.jpg")

#Create HSV color space from BGR. 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


threshholdBlue = np.array([110, 50, 50])
lowerBlue = np.array([130,255,255])

#provide thresholding. 
mask = cv2.inRange(hsv, threshholdBlue, lowerBlue)

#Final result omitted from contour detectoin. 
#res = cv2.bitwise_and(image, image, mask=mask)



#ret,thresh = cv2.threshold(hsv,127,255,0)
#im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Draw Contours. 

#cv.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow("Image", image)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

