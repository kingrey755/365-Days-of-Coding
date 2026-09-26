import numpy as np, matplotlib.pyplot as plt

x, y = np.random.rand(2, 50)
colors, area = np.random.rand(50), (30 * np.random.rand(50))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.6, cmap='viridis')
plt.show()
