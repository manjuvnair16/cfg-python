import turtle

def draw_square(side_length, angle):
    turtle.color('green', 'yellow')
    turtle.begin_fill()

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()


draw_square(100, 90)

turtle.done()