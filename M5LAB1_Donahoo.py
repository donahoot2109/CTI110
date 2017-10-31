# CTI-110
# M5LAB1 - Shapes
# Timothy Donahoo
# 22OCT17

#initialize
import turtle     # Allows us to use turtles
win = turtle.Screen() #Creates a playground for turtles
win.bgcolor('lightblue')

# make your turtle
square = turtle.Turtle()      #Create a turtle, assign to t
square.shape("turtle")   # Gives shape to turtle
triangle = turtle.Turtle()
triangle.shape("turtle")  # Triangle shape

# turtle making a square
square.forward(50)
square.left(90)
square.forward(50)
square.left(90)
square.forward(50)
square.left(90)
square.forward(50)
square.left(90)

square.right(180)                           # Moves square turtle away from triangle turtle
square.forward(80)

# turtle making a triangle
triangle.forward(80)
triangle.left(120)
triangle.forward(80)
triangle.left(120)
triangle.forward(80)
triangle.left(120)



# at the end, keep the window open until closed
win.mainloop() # wait for user to close window

