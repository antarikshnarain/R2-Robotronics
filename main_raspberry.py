# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 05:12:15 2016

@author: antariksh
"""

# Running Programs as threads
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        if self.threadID==1:
            execfile('serverVideo1.py')
        elif self.threadID==2:
            execfile('joystickRecv.py')
        print "Exiting " + self.name

# Create new threads
thread1 = myThread(1, "Thread-Video")
thread2 = myThread(2, "Thread-Joystick")

# Start new Threads
thread2.start()
thread1.start()

print "Exiting Main Thread"
