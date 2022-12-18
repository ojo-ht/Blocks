from scipy.stats import cauchy
import numpy as np
import matplotlib.pyplot as plt

scale_parameters = np.geomspace(2,10,3)

x = np.linspace(cauchy.ppf(0.01), cauchy.ppf(0.99), 1000)

fig, ax = plt.subplots()

for scale_parameter in scale_parameters:
    ax.plot(x, cauchy.pdf(x, scale=scale_parameter))

ax.set_xlim(cauchy.ppf(0.01), cauchy.ppf(0.99))
ax.axis('off')
plt.show()
