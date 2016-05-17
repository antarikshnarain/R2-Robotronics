# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 04:29:58 2015

@author: antariksh
"""

# Server 2 
# To Send Video Output
import socket
import cv2


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host name == ''-> all connections accepted 
host = ''#socket.gethostname() 
port = 6000
s.bind((host,port))
s.listen(5)
#filename=raw_input('Enter Filename:')
#f=open(filename,'rb')  # reading file in binary format    
c, addr = s.accept()
print 'Got Connected to', addr, c
i=0    
vc=cv2.VideoCapture(0)
while True:
    if vc.isOpened():
        rval,frame = vc.read()
    else:
        rval=False
    if rval:
        frame = frame.flatten()
        data = frame.tostring()
        c.send(data)
        c.recv(4)
        print 'Completed'
c.close
s.close

