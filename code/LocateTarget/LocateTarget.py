import cv2, cv
import numpy as np
import sys

DP = 4
MIN_DISTANCE = 10
EDGE_THRESHOLD = 10
CENTER_THRESHOLD = 175
MIN_RADIUS = 2
MAX_RADIUS = 20

if len(sys.argv)>1:
    filename = sys.argv[1]
else:
    filename = 'p.png'

img_gray = cv2.imread(filename,cv2.CV_LOAD_IMAGE_GRAYSCALE)

if img_gray == None:
  print "cannot open ",filename

else:
  img = cv2.GaussianBlur(img_gray, (0,0), 3)
  aimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
  (flag, cimg) = cv2.threshold(img, 175, 250, cv2.THRESH_BINARY)
  circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,DP,MIN_DISTANCE,param1=EDGE_THRESHOLD, param2=CENTER_THRESHOLD, minRadius=MIN_RADIUS,maxRadius=MAX_RADIUS)
try:
  circles = np.uint16(np.around(circles))
  for target in circles[0,:]:
    print(target)
    x = target[0]
    y = target[1]
    r = target[2]
    cv2.circle(aimg,(x,y,r,(0,255,0),1) 
    cv2.circle(aimg,(x,y),2,(0,0,255),3)   
except AttributeError:
  print('None detected')

cv2.imshow('blurred image',aimg)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()