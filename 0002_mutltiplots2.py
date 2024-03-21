# nrows, ncols, plot number

x = np.arange(0, 100, 10)

y = 3 * x ** 2 - 1

z = x ** 2 + 3

plt.subplot(2, 1, 1)

plt.title("x vs y")

plt.plot(x, y, "b")

plt.subplot(2, 1, 2)

plt.title("x vs z")

plt.plot(x, z, "r--")

plt.show()
