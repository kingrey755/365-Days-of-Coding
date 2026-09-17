import numpy as np
import matplotlib.pyplot as plt

nums = np.arange(1, 1001)
prime = np.ones(len(nums), dtype=bool)

for p in range(2, 32):
    if prime[p-2]:
        prime[p*p-2::p] = False
        
plt.figure(figsize=(8, 8))
plt.imshow(prime.reshape(40, 25), interpolation="nearest")
plt.axis("off")
plt.show()
