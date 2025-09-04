import turtle
wn = turtle.Screen() #Creating turtle window
wn.bgcolor("lightblue")
alex = turtle.Turtle() # crating turtle 
alex.pencolor("red")
alex.pensize(5)

distance = 50
for _ in range(10):
    alex.forward(distance)
    alex.left(90)
    distance += 10


print("Turtle Created!")
wn.exitonclick()