import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100) * 10
y = np.random.rand(100) * 10
plt.scatter(x, y, alpha=0.7, c="crimson")
plt.show()
