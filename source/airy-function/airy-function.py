import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# Real

x = np.linspace(-100, 10, 20000)
ai, aip, bi, bip = special.airy(x)

fig, ax = plt.subplots()

ax.plot(x, ai, 'r', label='Ai(x)')
ax.plot(x, bi, 'b--', label='Bi(x)')

ax.set_ylim(-0.5, 1.0)
ax.legend(loc='upper left')

plt.show()

# Complex

real = np.linspace(-10,10,100)
imag = real

