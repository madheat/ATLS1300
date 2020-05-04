# Final Project
# Madi Heath, Todd Holce, Mckenna Gray
# 04102020
"""
This code will generate different polygon art each time it runs all based on my color pallette of yellow
"""

import pygame
from random import * 
import time
import numpy

pygame.init()

FPS = 5 #frames per second setting 2 lines of code found on https://riptutorial.com/pygame/example/17502/drawing-and-a-basic-animation
fpsClock = pygame.time.Clock() 

#screen setup
size = (500,500)
screen = pygame.display.set_mode(size)
run = True

x1 = 240
x2 = 250
x3 = 260
x4 = 270
x5 = 280
y1 = 260
y2 = 240
y3 = 260
y4 = 270
y5 = 250

#define function
def drawTriangles(color):
    ''' draws polygons with random xy points '''
    pygame.draw.polygon(screen, colorList[i%4], [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5)], width) #creates triangles with x,y coordinate points

#run loop
while run:

    keys = pygame.key.get_pressed() # check for any keys etc. that are pressed 
    
    pygame.display.init
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
     # used to exit pygame when escape button is pressed
        elif keys[pygame.K_ESCAPE]:
            pygame.quit(); exit()
                        
    width = 2        
    
    #add animations, call functions to generate animations here
    for i in range(4):
        for i in range(4):
            for i in range(4):
                x1 += randint(-20,0)
                x2 += randint(-5,5)
                x3 += randint(0,20)
                x4 += randint(-20,10)
                x5 += randint(0,15)
                y1 += randint(0,20)
                y2 += randint(-20,0)
                y3 += randint(0,20)
                y4 += randint(-5,5)
                y4 += randint(-10,5)
                colorList = [(233, 189, 10),(236, 202, 56),(240, 215, 103),(243, 228, 149)]
                drawTriangles(colorList[i%4])


    #update the display and FPS 
    pygame.display.update()
    fpsClock.tick(FPS)
	
pygame.quit() 
