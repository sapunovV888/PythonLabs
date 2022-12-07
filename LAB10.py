import matplotlib.pyplot as plt
import numpy as np
import math



x = np.arange(1, 6, 1)
y = np.array([5 * math.cos(10 * i) * math.sin(3 * i) / (i ** 0.5) for i in x])
plt.xlabel('x') 
plt.ylabel('y')
plt.title('Function plot')
plt.plot(x, y, label = 'Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2)), x=[0...5]', color = "g", linewidth = 5)
plt.legend()
plt.show()

