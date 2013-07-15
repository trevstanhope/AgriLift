#!/usr/bin/python
# AgriLift
import cv2, cv
import numpy as np
import sys
from serial import SerialException
import serial

BAUD = 9600
DEVICE = '/dev/ttyACM0'
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
DP = 4
MIN_DISTANCE = 10
EDGE_THRESHOLD = 10
CENTER_THRESHOLD = 175
MIN_RADIUS = 2
MAX_RADIUS = 20
WIDTH = 640
HEIGHT = 480

class AgriLift:

  def __init__(self):
    try:
      print('Setting up Camera...')
      self.camera = cv2.VideoCapture(CAMERA_INDEX)
      self.camera.set(3,WIDTH)
      self.camera.set(4,HEIGHT)
      print('...Success.')
    except Exception:
      print('...Failure.')
    try:
      print('Setting up Controller...')
      self.arduino = serial.Serial(DEVICE, BAUD)
      print('...Success.')
    except Exception:
      print('...Failure.')
  
  ## Fly to Waypoint
  def fly_to_waypoint(self):

  ## Locate Bale
  def locate_bale(self):
    (success, frame) = self.camera.read()
    if success:
      grayscale = cv2.cvtColor(frame, cv.CV_BGR2GRAY)
      blurred = cv2.GaussianBlur(grayscale, (0,0), 3)
      colored = cv2.cvtColor(blurred,cv2.COLOR_GRAY2BGR)
      (flag, thresholded) = cv2.threshold(blurred, 175, 250, cv2.THRESH_BINARY)
      circles = cv2.HoughCircles(blurred,cv2.cv.CV_HOUGH_GRADIENT,DP,MIN_DISTANCE,param1=EDGE_THRESHOLD, param2=CENTER_THRESHOLD, minRadius=MIN_RADIUS,maxRadius=MAX_RADIUS)
    try:
      circles = np.uint16(np.around(circles))
      for target in circles[0,:]:
        x = target[0]
        y = target[1]
        r = target[2]
        cv2.circle(colored,(x,y),r,(0,255,0),1)
        cv2.circle(colored,(x,y),2,(0,0,255),3)
        cv2.imshow('colored', colored)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except AttributeError:
      print('None detected')

if __name__ == "__main__":
  drone = AgriLift()
  drone.fly_to_waypoint()
  drone.locate_bale()
