import turtle

no_of_sides = int(input('Enter the number of sides: '))
angle = 360 / no_of_sides

for side in range(no_of_sides):
    turtle.forward(100)
    turtle.right(angle)

turtle.done()