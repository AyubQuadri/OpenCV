import cv2
import numpy as np
img = cv2.imread('C:\\Users\\AyubQuadri\\Downloads\\Ouptut\\Ouptut\\100.bmp')
cv2.imwrite('bmpimg.bmp',img )
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 2560*(-b))
    y1 = int(y0 + 2560*(a))
    x2 = int(x0 - 2560*(-b))
    y2 = int(y0 - 2560*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imwrite('100.jpg',img)


import cv2
import numpy as np
img = cv2.imread('C:\\Users\\AyubQuadri\\Downloads\\Ouptut\\Ouptut\\20.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imwrite('20.jpg',img)  
