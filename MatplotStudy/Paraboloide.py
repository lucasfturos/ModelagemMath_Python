import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection="3d")


def f(x, y):
    return x**2 + y**2


x = np.linspace(-20, 20, 40)
y = np.linspace(-20, 20, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color="black")
# plt.axis("off")
ax.set_title("Paraboloide")
plt.show()
