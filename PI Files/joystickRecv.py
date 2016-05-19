# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 03:20:56 2016
@author: antariksh
"""
# Get Joystick Values
import socket
import serial
import time

# Initialize a Serial COM at 115200 Baud with Arduino
ser = serial.Serial('/dev/ttyACM0', 115200)
# Create Server for Joystick
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ''#socket.gethostname()
port = 5002
# Bind and Listen to Port for Server
s.bind((host,port))
s.listen(5)

c, addr = s.accept()
print "Connected to ",c,addr,
while True:
    data=c.recv(55) # Receive 55 bytes of Joystick Data
    """
    Extract Data From the String
   	"""
    data=data.strip() 
    if len(data)>0:
        arr = data.split(' ')
        for i in range(len(arr)):
            ser.write('<'+arr[i]+'>')
            print '<'+arr[i]+'>'
        print "Success"
    c.send('Done') # Send Acknowledgement
    #time.sleep(0.1)
ser.close()
