# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 00:44:51 2016

@author: antariksh
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 01:56:41 2016

@author: antariksh
"""

import pygame
pygame.init()
clock = pygame.time.Clock()
# Initialize the joysticks
pygame.joystick.init()
done=False
data=''
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
            #print axis
        buttons = joystick.get_numbuttons()
        for i in range( buttons ):
            button = joystick.get_button( i )
            #print button
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
            #print hat
        clock.tick(20)
        
pygame.quit ()