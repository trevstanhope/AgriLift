from cv2 import VideoCapture
import cv2, cv
import numpy as np
import sys
from serial import SerialException
import serial

BAUD = 9600
DEVICE = '/dev/ttyACM0'
CAMERA_INDEX = 1
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
DP = 4
MIN_DISTANCE = 10
EDGE_THRESHOLD = 10
CENTER_THRESHOLD = 175
MIN_RADIUS = 2
MAX_RADIUS = 20

class AgriLift:
  def __init__(self):
    try:
      print('Setting up Camera...')
      self.camera = VideoCapture(CAMERA_INDEX)
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
  def locate_bale(self):
    (success, frame) = self.camera.read()

if __name__ == "__main__":
  drone = AgriLift()
  drone.locate_bale()
