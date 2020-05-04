# PC03 - Generative Art
#
# Madi Heath
# 
# 20200212
#
# The Vatican is Secure
#
# This code will generate random spiral lasers of different greens over screen
# to imitate security lasers
#
from turtle import * 
import numpy as np
from random import * 

window = Screen()
window.screensize(800,600)
window.bgpic('vatican.gif')
window.update()

spiral = Turtle(visible=False)
spiral.speed(15)
size = 2

colors = ["#D7FFAB", "green", "#62A87C", "#7EE081"]
          
# creating 10 archimedean spirals, formula found on https://rosettacode.org/wiki/Archimedean_spiral#Python

for i in range(4):
    
    spiral.color(colors[i%4]) 
    start_x = randint(-250, 250)
    start_y = randint(-250, 250)
    new_x = randint(-100, 150)
    new_y = randint(-100, 150)
    r = randint(2,6)
    u = randint(1,3)
    
    # When brainstorming, I was originally going to crate spirals and not line spirals, but I liked 
    # how it turned out with changing where I place the goto functions better
    
    for i in range(200):
        spiral.up()
        spiral.goto(start_x, start_y)
        spiral.down()
        t = i / size * np.pi
        x = (u + r * t) * np.cos(t)
        y = (u + r * t) * np.sin(t)
        spiral.goto(x, y)
        spiral.up()
        new_x = randint(-100, 150)
        new_y = randint(-100, 150)
        spiral.goto(new_x, new_y)
    
    spiral.color(colors[i%4]) 
    spiral.goto(new_x, new_y)

done()