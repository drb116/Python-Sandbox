'''
Created on Mar 28, 2019

@author: drb11
'''

#from turtle import *
import turtle

window = turtle.Screen() #Don't need turtle with the from
adam = turtle.Turtle()# need turtle with the import
adam.speed("fastest")

def square(length):
    for i in range(4):
        adam.forward(length)
        adam.right(90)

def star(length, points):
    for i in range(points):
        square(length)
        adam.right(360/points)

def pedal(length):
    for i in range(2):
        adam.circle(length,60,360)
        adam.left(120)

def flower(length,pedals):
    for i in range(pedals):
        pedal(length)
        adam.right(360/pedals)


if __name__ == '__main__':
    colors = ["blue","red","green", "yellow"]
    size = 200

    for color in colors:
        adam.pencolor(color)
       # star(size,30)
        flower(size,30)
        size -=50
    window.exitonclick()
