# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 04:05:37 2015

@author: antariksh
"""

import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyWindow("preview")
