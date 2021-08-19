import turtle
turtle.color('green', 'yellow')
turtle.begin_fill()
for side in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.forward(150)
turtle.color('red', 'blue')
turtle.begin_fill()
for side in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.end_fill()
turtle.forward(150)
turtle.color('blue', 'red')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
for side in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.done()