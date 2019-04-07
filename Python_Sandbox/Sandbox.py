from turtle import *

win = Screen()
alex = Turtle()
alex.shape("turtle")

for i in range(4):
    alex.forward(100)
    alex.right(90)

win.exitonclick()
