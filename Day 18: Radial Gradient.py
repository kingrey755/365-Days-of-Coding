import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,500)
X,Y = np.meshgrid(x,x)
Z = 1 - np.sqrt(X**2 + Y**2)
plt.imshow(Z, cmap="Blues"); plt.axis("off"); plt.show()
