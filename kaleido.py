import turtle
from itertools import cycle
import random

colors = cycle(['red', 'green', 'orange', 'purple', 'blue'])

def draw_circle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)

    if random.random() < 0.5:
        print(f"CIRCLE {size} drawn!")
    else:
        print(f"CIRCLE {size} skipped!")

size = 30
angle = 0
shift = 1

for i in range(10):
    draw_circle(size, angle, shift)
    size += 5
    angle += 1
    shift += 1

turtle.done()
