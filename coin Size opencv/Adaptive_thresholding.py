# Adaptive thresholding to over come the shaded region
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('images/Adaptive_Threshold.jpg')
img = cv2.medianBlur(img,5)

ret, th1 = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
Title = ['Original image', 'Global Threshold (v=127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian']

images = [img, th1, th2, th3]

for i in xrange(3):
    plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
    plt.title(Title[i])
    plt.xticks([]),plt.yticks([])
plt.show()