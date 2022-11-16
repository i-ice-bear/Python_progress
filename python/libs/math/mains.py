import matplotlib.pyplot as plt
import numpy as np

_random_number_x_axis = np.random.randint(100, size=5)
_random_number_y_axis = np.random.randint(100, size=5)
x_histogram = np.random.normal(170, 10, 250)
__pie__array = np.array([20, 40, 20, 20])
__pie__labels = ["Apples", "Banana", "Mango", "Papaya"]
__pie__colors = ["Hotpink", "Lightblue", "Cyan", "Purple"]

plt.plot(_random_number_x_axis, _random_number_y_axis)
plt.show()
plt.hist(x_histogram)
plt.show()
plt.pie(__pie__array, labels=__pie__labels, colors=__pie__colors)
