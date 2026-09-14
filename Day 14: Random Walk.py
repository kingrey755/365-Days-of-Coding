import random
import matplotlib.pyplot as plt

steps = []
step = 0

for i in range(100):
    step += 1 if random.randint(1,2) == 1 else -1
    steps.append(step)

plt.scatter(range(100), steps)
plt.show()
