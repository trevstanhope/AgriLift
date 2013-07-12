from serial import SerialException
import serial

BAUD = 9600
DEVICE = '/dev/ttyACM0'

arduino = serial.Serial(DEVICE, BAUD)
while 1:
  gpgga = []
  raw_gps = arduino.readline()
  for line in raw_gps.split('\n'):
    if "$GPGGA" in line:
      for gps_value in line.split(','):
        gpgga.append(gps_value)
      print(gpgga)
        
