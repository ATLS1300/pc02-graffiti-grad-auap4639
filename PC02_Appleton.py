#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "B.gif"
panel.bgcolor("steelblue1")
panel.bgpic(image)

#=======Add your code here======
from turtle import *
color('green')
pensize(20)
up()
goto(10,120)
down()
goto(35,0)
up()
goto(50,120)
dot(50,'yellow')
up()
goto(-30,110)
dot(50,'magenta')
goto(-6,160)
pensize(3)
color(80,20,100)
down()


REPEATS = range(6)

for element in REPEATS:
    forward(20)
    left(60)


up()
goto(-170,-20)
pen(pencolor="red", fillcolor="white",pensize=7,speed=9)
begin_fill()

REPEATS = range(3)

for element in REPEATS:
    forward(75)
    left(120)
end_fill()

up()
goto(100,-20)
pen(pencolor="red", fillcolor="black",pensize=7,speed=9)

begin_fill()

REPEATS = range(3)

for element in REPEATS:
    forward(75)
    right(120)
end_fill()


done()