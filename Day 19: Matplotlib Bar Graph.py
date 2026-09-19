import matplotlib.pyplot as plt
import random

plt.bar(range(1, 5), [random.randint(1, 100) for _ in range(4)])
plt.show()
