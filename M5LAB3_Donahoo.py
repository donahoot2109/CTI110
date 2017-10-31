# CTI-110
# M5LAB3 - Snowflake
# Timothy Donahoo
# 22OCT17

# import turtle
import turtle

# Name your turtle

myPen = turtle.Turtle()
myPen.shape('turtle')
myPen.speed(500)


myPen.color('blue')

# use commands to creat your snowflake

myPen.left(90)

for i in range(0,6):
    myPen.forward(100)
    myPen.forward(-40)
    myPen.left(40)
    myPen.forward(30)
    myPen.forward(-30)
    myPen.right(80)
    myPen.forward(30)
    myPen.forward(-30)
    myPen.left(40)
    myPen.forward(-60)

    myPen.right(60)


