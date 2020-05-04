# 
# PC04 Interactive robot
# 
# 02192020
# 
# Madi Heath
#
# Dwarf fortress robot friends will move around and dominate all dwarves in their
# fortress
#
# Not really but they will move around and their eyes will change colors because anger
#
'''
PSUEDOCODE
import pygame and random
set colors and variables 
create background on dwarf fortress
in game loop:
    create a robot that has a square head and square body with four wheels 
    create a second robot exactly the same but peach
    create eyes and panel lights
    if: pressing the return changes the color of its eyes, backspace reverts back to yellow
    elif: moves the robot left, right, up, down
    elif: asdw moves other robot
    elif: press escape to exit

uses parts of example robot script given on canvas
'''

import pygame
from random import * 
import time

pygame.init()

# sets up colors 
LIGHTBLUE = (151,255,255)
PINK = (238,18,137)
YELLOW = (255,215,0)
PEACH = (255,160,122)
GREEN = (162,205,90)
BLACK = (0,0,0)
WHITE = (255,255,255)
CREAM = (255,248,220)
RED = (255,0,0)
BLUE = (0,0,255)


size = 500 
screen = pygame.display.set_mode((500,500))
myImage = pygame.image.load("dwarffortress.gif")
imageRect = myImage.get_rect()

# discovered set_caption to display a title/caption on window just for fun
pygame.display.set_caption("Robot Bois in a Dwarf Fortress World")

# variables and such 
run = True
x = size/2
y = size/2
xX = size/2
yY = size/2
scale = 1
speed = 10
eye_r = 3

# eyes
eyeColor = YELLOW

# game loop
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
    # screen things        
    screen.blit(myImage,imageRect)
    pygame.display.flip()
    
    
    # robo body parts
    Head = pygame.draw.rect(screen, LIGHTBLUE, (x-25,y-90,50,50))
    Body = pygame.draw.rect(screen, LIGHTBLUE, (x-35, y-35,75,75))
    L_eye = pygame.draw.circle(screen, eyeColor, (int(x-10), int(y-70)),eye_r)
    R_eye = pygame.draw.circle(screen, eyeColor, (int(x+10), int(y-70)),eye_r)
    lights1 = pygame.draw.circle(screen, RED, (int(x+20), int(y-5)),3)
    lights2 = pygame.draw.circle(screen, BLUE, (int(x), int(y-5)),3)
    lights3 = pygame.draw.circle(screen, GREEN, (int(x-20), int(y-5)),3)
    
    firstWheel = pygame.draw.circle(screen, PINK, (int(x-40), int(y+55)),10,5)
    secondWheel = pygame.draw.circle(screen, PINK, (int(x+40), int(y+55)),10,5)
    thirdWheel = pygame.draw.circle(screen, PINK, (int(x-15), int(y+55)),10,5)
    lastWheel = pygame.draw.circle(screen, PINK, (int(x+15), int(y+55)),10,5)
    
    # second robo body parts
    HeadTwo = pygame.draw.rect(screen, PEACH, (xX-25,yY-90,50,50))
    BodyTwo = pygame.draw.rect(screen, PEACH, (xX-35, yY-35,75,75))
    L_eyeTwo = pygame.draw.circle(screen, eyeColor, (int(xX-10), int(yY-70)),eye_r)
    R_eyeTwo = pygame.draw.circle(screen, eyeColor, (int(xX+10), int(yY-70)),eye_r)
    lights1Two = pygame.draw.circle(screen, RED, (int(xX+20), int(yY-5)),3)
    lights2Two = pygame.draw.circle(screen, BLUE, (int(xX), int(yY-5)),3)
    lights3Two = pygame.draw.circle(screen, GREEN, (int(xX-20), int(yY-5)),3)
    
    firstWheelTwo = pygame.draw.circle(screen, PINK, (int(xX-40), int(yY+55)),10,5)
    secondWheelTwo = pygame.draw.circle(screen, PINK, (int(xX+40), int(yY+55)),10,5)
    thirdWheelTwo = pygame.draw.circle(screen, PINK, (int(xX-15), int(yY+55)),10,5)
    lastWheelTwo = pygame.draw.circle(screen, PINK, (int(xX+15), int(yY+55)),10,5)
    
    
    keys = pygame.key.get_pressed() # check for any keys that are pressed
    
    # moves blue robot
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # moves peach robot
    if keys[pygame.K_d]:
        xX += speed
    if keys[pygame.K_a]:
        xX -= speed
    if keys[pygame.K_w]:
        yY -= speed
    if keys[pygame.K_s]:
        yY += speed
    
    # changes eye color
    if keys[pygame.K_RETURN]:
        eyeColor = RED    
    if keys[pygame.K_BACKSPACE]:
        eyeColor = YELLOW
        
    # used to escape pygame when pressing escape
    # the exit function was found on stack overflow by an anonymous user
    elif keys[pygame.K_ESCAPE]:
        pygame.quit(); exit()
    
    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    