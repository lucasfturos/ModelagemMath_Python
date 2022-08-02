import turtle as t
from math import atan2

t.speed(0.000001)
t.pensize(1)
t.pencolor("black")
t.radians()
t.pendown()

dt, sig, rho, b = 0.01, 10, 28, 2.667
x, y, z = 0.0, 1.0, 1.05
dx, dy, dz = 0.0, 0.0, 0.0
escala = 13

while True:
    t.setpos(x * escala, y * escala)
    t.setheading(atan2(dy, dx))

    dx = (sig * (y - x)) * dt
    dy = (rho * x - y - x * z) * dt
    dz = (x * y - b * z) * dt

    x += dx
    y += dy
    z += dz
