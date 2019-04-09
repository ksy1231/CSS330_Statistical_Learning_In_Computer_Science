import numpy as np
import matplotlib.pyplot as plt
'''
# plot sine curve 
radians = np.arange(31)/30*2.0*np.pi
sines = np.sin(radians)
plt.plot(radians, sines)

# plot 15 points on the sine curve
x = np.linspace(0, 2*np.pi, 15)
y = np.sin(x)
plt.scatter(x,y)
'''
x = np.arange(15) / 14.0 * (2 * np.pi)
y = np.sin(x)
plt.plot(x, y, 'bo-')
# name label
plt.xlabel("Radians")
plt.ylabel("Sine")

plt.show()