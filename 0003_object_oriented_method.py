#object_oriented_method

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100, 10)

y = 3 * x ** 2 - 1

#create figure
figure = plt.figure()

axes = figure.add_axes(rect = [0.2, 0.2, 0.6, 0.6]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'g')
axes.set_xlabel("x values")
axes.set_ylabel("y values")
axes.set_title("x vs y")
