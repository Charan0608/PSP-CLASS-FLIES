import turtle

turtle.bgcolour("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["red","blue","green","white","orange","yellow","cyan"]:
        turtle.colour(colour)
        turtle.circle(100)
        turtle.left(10)

    turtle.hideturtle()
