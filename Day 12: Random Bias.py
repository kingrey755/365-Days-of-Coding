import random
import matplotlib.pyplot as plt

coords=[[random.random() for i in range(1000)] for i in range(3)]
fig=plt.figure()
ax=fig.add_subplot(projection="3d")
ax.scatter(*coords, alpha=0.5, s=10)
plt.show()
