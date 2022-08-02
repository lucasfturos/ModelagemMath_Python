import matplotlib.pyplot as plt
import numpy as np

theta = np.arange(0, 4 * np.pi, 0.001)
x = np.cos(theta) * (
    np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta / 4) ** 3
)
y = np.sin(theta) * (
    np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta / 4) ** 3
)

plt.plot(x, y, color="black", linewidth=1.0)
plt.title("Borboleta")
plt.show()
