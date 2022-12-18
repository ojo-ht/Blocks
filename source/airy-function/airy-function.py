import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# Real

x = np.linspace(-10, 6, 1000)
ai, aip, bi, bip = special.airy(x)

fig, axes = plt.subplots(2, 1, sharex=True) # 0 top, 1 bottom

axes[0].plot(x, ai, 'r', label='Ai(x)')
axes[1].plot(x, bi, 'b--', label='Bi(x)')

for axis in axes:
    axis.set_ylim(-0.5, 1.0)
    axis.set_yticks([])
    axis.legend(loc='upper left')
    axis.axis('off')

axes[1].set_xlim(x.min(), x.max())
plt.show()

# Complex

real = np.linspace(-10,10,100)
imag = real

