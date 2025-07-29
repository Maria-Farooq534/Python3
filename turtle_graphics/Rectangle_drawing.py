import turtle
wn = turtle.Screen() # it will create a screen for turtle.
wn.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.color("green")
tess.pensize(5)

tess.forward(100)
tess.left(120)
tess.forward(100)
tess.left(120)
tess.forward(100)
tess.left(120) # triangle complete

tess.right(180)
tess.forward(50)

alex = turtle.Turtle() # create a turtle named alex
alex.pencolor("red")
alex.pensize(3)
alex.forward(150)
alex.left(90)  #We invoke a method left() and pass a parameter 90
alex.forward(75)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)




wn.exitonclick()


# tess = turtle.Turtle()           # create tess and set his pen width
# tess.pensize(5)

# alex = turtle.Turtle()           # create alex
# alex.color("hotpink")            # set his color

# tess.forward(80)                 # Let tess draw an equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)                   # complete the triangle

# tess.right(180)                  # turn tess around
# tess.forward(80)                 # move her away from the origin so we can see alex

# alex.forward(50)                 # make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

# wn.exitonclick()