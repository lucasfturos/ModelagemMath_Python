from matplotlib.pyplot import plot, title, show, gcf
from numpy import tanh, sin, cos, arange, pi

a = 1
b = 10
n = 12

t = arange(0, 2 * pi, 0.01)
r = a + (1 / b) * (tanh(b * sin(n * t))) * cos(t)
x = r * cos(t)
y = r * sin(t)

plot(x, y, color="black", linewidth=1.0)
title("Engrenagem")
show()
