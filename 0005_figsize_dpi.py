#figsize_dpi

#dpi dots per inch, pixel per inch

figure = plt.figure(figsize = (12, 6), dpi = 80)

axes = figure.add_axes(rect = [0.4, 0.4, 0.6, 0.6]) 

axes.plot(x, y, "r")

axes.set_xlabel("x values")
axes.set_ylabel("y values")
axes.set_title("x vs y")

