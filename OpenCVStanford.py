'''
 * Python program to use contours to count the objects in an image.
 *
 * usage: python Contours.py <filename> <threshold>
'''
import cv2, sys



# read original image
filename = sys.argv[1]
t = int(sys.argv[2])

print("Filename and threshold value noted.  ")

image = cv2.imread(filename)

# create binary image
# create binary image
gray = cv2.cvtColor(
    src = image, 
    code = cv2.COLOR_BGR2GRAY)
blur = cv2.Gaussian Blur(
    src = gray, 
    ksize = (5, 5), 
    sigmaX = 0)
t, binary = cv2.threshold(
    src = blur,
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY)

im2, contours, hierarchy = cv2.findContours(image = binary,
 mode = cv2.RETR_EXTERNAL, 
 method = cv2.CHAIN_APPROX_SIMPLE)
 
cv2.imshow(gray)
cv2.imshow(blur)
