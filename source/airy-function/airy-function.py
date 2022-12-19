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


# Complex

real = np.linspace(-10,10,100)
imag = real

nx, ny = (301, 301)

x = np.linspace(-7, 7, nx)
y = np.linspace(-7, 7, ny)

xv, yv = np.meshgrid(x, y)

complex_grid = np.zeros(xv.shape, dtype=np.complex_)

complex_grid.real = xv
complex_grid.imag = yv

ai, aip, bi, bip = special.airy(complex_grid)

bi_imag = np.clip(bi.imag, -2.5, 2.5)

fig3, ax3 = plt.subplots()
ax3.contourf(xv, yv, bi_imag, levels=20, cmap='magma')
ax3.contour(xv, yv, bi_imag, levels=20, colors='k',  linestyles='solid')
ax3.axis('off')
ax3.set_position([0, 0, 1, 1])



fig4 = plt.figure()
ax4 = fig4.add_subplot(projection='3d')
ax4.plot_surface(xv, yv, bi_imag, cmap='magma', linewidth=0, rstride=5, cstride=5)
ax4.set_position([0, 0, 1, 1])
ax4.xaxis.set_ticklabels([])
ax4.yaxis.set_ticklabels([])
ax4.zaxis.set_ticklabels([])

for line in ax4.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax4.yaxis.get_ticklines():
    line.set_visible(False)
for line in ax4.zaxis.get_ticklines():
    line.set_visible(False)

ax4.view_init(elev=49, azim=-116, roll=0)

fig3.savefig('/home/josep/Documents/Blocks/docs/chapter-2-special-functions/airy-function/images/airy-contour-highdpi.png', format='png', dpi=1200)
fig4.savefig('/home/josep/Documents/Blocks/docs/chapter-2-special-functions/airy-function/images/airy-3dsurf-highdpi.png', format='png', dpi=1200)

plt.show()
