# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 01:56:41 2016

@author: antariksh
@Organization: R2 Robotics
"""

import pygame
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host name == ''-> all connections accepted 
"""
To get the IP Address of Raspberry PI
Shell $hostname -I
Shell $arp -a | grep eth0
->Will give you the IP of the connected system
"""

host = '10.42.0.77'#IP Address of Raspberry PI #socket.gethostname() 
port = 5002
s.connect((host,port))
pygame.init()
clock = pygame.time.Clock()
# Initialize the joysticks
pygame.joystick.init()
done=False
data=''
#Data format of Joystick Data
olddata='0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0'

# String intersection Function
def dataValue(a,b):
    sendData=''
    for i in range(len(a)):
        if a[i]!=b[i]:
            sendData=sendData+str(i)+str(b[i])+' '
    return sendData
# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    data=''
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        print name        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )
            data=data+str("%.0f"%(axis*255))+' '           
            #print axis
        buttons = joystick.get_numbuttons()
        for i in range( buttons ):
            button = joystick.get_button( i )
            data=data+str(button)+' '
            #print button
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
            myHats=str(hat)            
            # Extracting data from hat Values (0,0)
            b=myHats.split(',')[0].split('(')[1]
            c=myHats.split(', ')[1].split(')')[0]            
            data=data+b+' '+c
            #print hat
        clock.tick(20)
        arr1=data.split(' ')
        arr2=olddata.split(' ')
        sendData=' '
        for i in range(len(arr1)):
            if arr1[i] not in arr2[i]:
                sendData=sendData+chr(i+65)+arr1[i]+' '
        print sendData
        s.send(sendData)
        olddata=data
        s.recv(4) # Receive an Acknowledgement
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
