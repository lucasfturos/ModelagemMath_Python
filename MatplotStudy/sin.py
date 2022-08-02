import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0, 20, 0.1)
y1 = np.sin(x1)

plt.plot(x1, y1, color="black", linewidth=1.0)
plt.title("Seno")
plt.show()
