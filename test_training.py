import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.cos(x)
plt.plot(x,y)
plt.ylabel('y')
plt.xlabel('x')
plt.show()