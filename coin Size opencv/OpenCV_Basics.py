import cv2
import numpy as np 
from matplotlib import pyplot as plt

# read image
img = cv2.imread('images/mainimage.jpg')

# image shape & size 
print(img.shape)
print(img.size)

# splitting of image in openCV
b,g,r = cv2.split(img)
new_img = cv2.addWeighted(b,0.7,g,0.3,0)
# Arithimatic operations on images
# There is a difference between OpenCV addition and Numpy addition. 
# OpenCV addition is a saturated operation 
# while Numpy addition is a modulo operation.
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y))  # 260 + 10 = 260 => 255

print(x+y)  # 260+10 = 260% 256 = 4
    # displaying the images using opencv
cv2.imshow('Detected',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# image blending

img1_path ='pics/2.jpg'
img2_path ='pics/9.jpg'

img1 = cv2.imread('pics/2.jpg')
b,g,r =cv2.split(img1)

new_img = cv2.addWeighted(r,0.7,g,0.3,0)

cv2.imshow('blended_Image',new_img)
cv2.waitKey(0)'
cv2.destroyAllWindows()