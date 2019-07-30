import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np
import ctypes

def Mbox(title, text, style):
  return cytypes.windll.user32.MessageBox32.MessageBoxW(0, text, title, style)

Mbox("vars","input",1)

# read original image
filename = sys.argv[1]

print("Filename and threshold value noted.  ")
#image input. 
image = cv2.imread(filename)


def histogram(filename):
    processImage = cv2.imread(
        #filename declaration
        filename = filename, 
        #greyscale preprocessing
        flags = cv2.IMREAD_GRAYSCALE)

    #histogram is a one dimensional numpy array. 
    histogram = cv2.calcHist(
        #list of images.
        images = [processImage],
        #list of channels for image examination. 
        channels = [0],
        #no mask.
        mask = None,
        #Number of bins for the histogram. 
        histSize = [256],
        ranges = [0,256])
    
    #print(histogram)

    # configure and draw the histogram figure
    plt.figure()
    plt.title("Greyscale Histogram Analysis")
    plt.xlabel("Pixel Value")
    plt.ylabel("Pixels")
    plt.xlim([0, 256]) # <- named arguments do not work here

    plt.plot(histogram) # <- or here
    plt.show()

    #return histogram
    return histogram

def histogramAnalysis(histogram):
    maxVal = np.amax(histogram)
    return type(maxVal)


    
#calling the histogram function
histogram(filename)
#print(histogramAnalysis(histogram(filename)))
# create binary image
# create binary image

#The pixels of value t will be turned 'off'
#Fixed level thresholding
t = int(input("Enter threshold value"))

def find_contours(binary):
    #return second parameter in tuple, ignore rest of returnVals.
    intermediary ,contours = cv2.findContours(image = binary, mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
    return contours

#Thresholding and image processing. 
gray = cv2.cvtColor(
    src = image, 
    code = cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(
    src = gray, 
    ksize = (5, 5), 
    sigmaX = 0)
t, binary = cv2.threshold(
    src = blur,
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY_INV)

contour_array = find_contours(binary)

print("contours found")
print(len(contour_array))

cv2.drawContours(image = binary, 
    contours = contour_array, 
    contourIdx = -1, 
    color = (0, 0, 255), 
    thickness = 5)

cv2.imshow("processed image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


