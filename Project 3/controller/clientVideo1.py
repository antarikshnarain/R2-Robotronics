# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 04:30:22 2015

@author: antariksh
"""
# Client 2 
# To Receive Video Input
import socket
import cv2
import numpy

cv2.namedWindow("preview")    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '10.42.0.77'#socket.gethostname()
port = 6000

#filename=raw_input('Enter Filename to Save as:')
#f=open(filename,'w')
s.connect((host,port))
while True:
    data=s.recv(921600)
    # reading from buffer twice 
    while len(data)<921600:
        data=data+s.recv(921600)
        if len(data)==921600:
            break
    print len(data)
    s.send('Done')
    frame = numpy.fromstring(data, dtype=numpy.uint8)
    frame = numpy.reshape(frame, (480,640,3))
    print numpy.shape(frame)
    #s.send('Done')
    cv2.imshow("preview", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
s.close()
