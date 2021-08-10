import turtle

turtle.bgcolour("brown")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["red", "blue","cyan","yellow","orange","white"]:
        turtle.colour(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()        
