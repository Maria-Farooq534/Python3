import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

alex = turtle.Turtle()
alex.pencolor("red")
alex.pensize(5)
alex.shape("turtle")
alex.fillcolor("yellow")
alex.speed(5)
alex.begin_fill()
alex.end_fill()

alex.penup()
for _ in range(10):
    alex.forward(50)
    alex.stamp()
    alex.forward(-50)
    alex.right(36)
    

print(alex.heading())
print(alex.position())
wn.exitonclick()