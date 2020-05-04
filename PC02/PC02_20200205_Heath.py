# PC02 Animating with Turtles
# Madi Heath
# 20200205
# Using turtles to make animations

from turtle import *
import numpy as np

window = Screen()
window.screensize(600,600)
window.bgcolor("black")
window.update()

colors = ["#A5C4D4", "#8499B1", "#7B6D8D", "#6C3A5C", "#36151E", "#8D80AD", "#99B2DD", "#2F243A", "#7A6F9B", "#BEB8EB", "#8DA7BE", "#A997DF"]
turtleSpeed = ["slow", "normal", "fast", "fastest"]
          
spiral = Turtle()
spiral.shape("triangle")
spiral.shapesize(0.25, 0.25)
spiral.color("#A5C4D4")
spiral.pensize(3)
side = 10

spiralTwo = Turtle()
spiralTwo.shape("triangle")
spiralTwo.shapesize(0.25, 0.25)
spiralTwo.color("#A5C4D4")
spiralTwo.pensize(3)

spiralThree = Turtle()
spiralThree.shape("triangle")
spiralThree.shapesize(0.25, 0.25)
spiralThree.color("#A5C4D4")
spiralThree.pensize(3)

spiralFour = Turtle()
spiralFour.shape("triangle")
spiralFour.shapesize(0.25, 0.25)
spiralFour.color("#A5C4D4")
spiralFour.pensize(3)

for i in range(80):
  spiral.color(colors[i%12])
  spiral.forward(side)
  spiral.right(122)
  # a friend of mine explained the modulo function to me so that my colors would repeat
  # rather than saying the index is out of range :) 
  spiralTwo.color(colors[i%12])
  spiralTwo.forward(side)
  spiralTwo.left(122)
  
  spiralThree.color(colors[i%12])
  spiralThree.left(122)
  spiralThree.forward(side)
    
  spiral.speed(turtleSpeed[i%4])
  spiralTwo.speed(turtleSpeed[i%4])
  spiralThree.speed(turtleSpeed[i%4])
  side = side+15

spiral.hideturtle()
spiralTwo.hideturtle()
spiralThree.hideturtle()

done()