import matplotlib.pyplot as plt

import numpy as np

x = np.arange(0, 100, 10)

y = 2 * x ** 2 - 3

print(x)

print(y)

plt.plot(x, y, 'b') #blue

plt.xlabel("x values")

plt.ylabel("y values")

plt.title("y = 2 * x * x - 3")

plt.show()
