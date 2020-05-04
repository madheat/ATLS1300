
# PC01 Drawing Graffiti
# Madi Heath, Josie Davison
# 20200128
# Using turtles to draw a spiral shape then smiley face

from turtle import * 

window = Screen()
window.screensize(1400,1400)
window.bgpic("clairoforfun.gif") 
window.update()

spiralTurtle = Turtle()
spiralTurtle.shape("circle")
spiralTurtle.color("#DCD6F7", "#A6B1E1")
spiralTurtle.pensize(2)
spiralTurtle.speed('fast')

for i in range(240):
    spiralTurtle.forward(i)
    spiralTurtle.left(45)
spiralTurtle.hideturtle()

smileTurtle = Turtle()
smileTurtle.shape("circle")
smileTurtle.color("#985F6F")

smileTurtle.goto(0,-80)
smileTurtle.begin_fill()
smileTurtle.circle(80)
smileTurtle.end_fill()

smileTurtle.color("#DCD6F7")
smileTurtle.up()
smileTurtle.goto(-30,30)
smileTurtle.stamp()
smileTurtle.goto(30,30)
smileTurtle.stamp()
smileTurtle.goto(-40,-30)
smileTurtle.setheading(-40)
smileTurtle.width(5)
smileTurtle.down()
smileTurtle.circle(60,80)
smileTurtle.up()
smileTurtle.hideturtle()

done()