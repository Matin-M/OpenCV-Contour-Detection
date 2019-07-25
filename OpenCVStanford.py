import cv2
import sys
from matplotlib import pyplot as plt

# read original image
filename = sys.argv[1]
#The pixels of value t will be turned 'off'
t = int(sys.argv[2])
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
    
    print(histogram)

    # configure and draw the histogram figure
    plt.figure()
    plt.title("Matin's Greyscale Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Pixels")
    plt.xlim([0, 256]) # <- named arguments do not work here

    plt.plot(histogram) # <- or here
    plt.show()

    #return histogram

    
#calling the histogram function
histogram(filename)

# create binary image
# create binary image
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
    type = cv2.THRESH_BINARY)



# main function. 

