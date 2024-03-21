import matplotlib.pyplot as plt

import numpy as np

x = np.arange(0, 100, 10) 

y = 2 * x ** 2 - 3 

print(x) # [ 0 10 20 30 40 50 60 70 80 90]

print(y) # [   -3   197   797  1797  3197  4997  7197  9797 12797 16197]

plt.plot(x, y, 'b') #blue

plt.xlabel("x values")

plt.ylabel("y values")

plt.title("y = 2 * x * x - 3")

plt.show()
