#object_oriented_method_multiple_plots

figure = plt.figure()

axes1 = figure.add_axes([0.0, 0.1, 0.8, 0.8]) 

axes2 = figure.add_axes([0.1, 0.5, 0.4, 0.3])

axes1.plot(x, y, 'g')
axes1.set_xlabel('x values')
axes1.set_ylabel('y values')
axes1.set_title('x vs y')


axes2.plot(y, x, 'b')
axes2.set_xlabel('y values')
axes2.set_ylabel('x values')
axes2.set_title('y vs x')
