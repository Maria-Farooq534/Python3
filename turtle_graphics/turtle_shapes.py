import turtle
wn = turtle.Screen()
wn.bgcolor("blue")

alex = turtle.Turtle()
alex.pencolor("red")
alex.pensize(5)

distance = 5
alex.down()        # will move up or down on down() method.
for _ in range(50):
    alex.stamp()
    alex.shape("turtle") #Other Shapes: arrow, blank, circle, classic, square, triangle, turtle.
    alex.forward(distance)
    alex.right(24)
    distance += 2


wn.exitonclick()