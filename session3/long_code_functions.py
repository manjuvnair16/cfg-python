import turtle

def draw_square(side_length, pen_color, fill_color):
    turtle.color(pen_color, fill_color)
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(side_length, pen_color, fill_color):
    turtle.color(pen_color, fill_color)
    turtle.begin_fill()
    for side in range(3):
        turtle.forward(side_length)
        turtle.right(120)
    turtle.end_fill()

def draw_circle(radius, pen_color, fill_color):
    turtle.color(pen_color, fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


draw_square(100,'green', 'yellow')
turtle.forward(150)
draw_triangle(100, 'red', 'blue')
turtle.forward(150)
draw_circle(50, 'blue', 'red')
draw_square(100,'green', 'yellow')
turtle.done()