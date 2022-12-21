import numpy as np
import matplotlib.pyplot as plt
from scipy import special

# Define plot parameters

colormap = 'gist_ncar'


# Real

x = np.linspace(-10, 6, 1000)
ai, aip, bi, bip = special.airy(x)

fig, axes = plt.subplots(2, 1, sharex=True) # 0 top, 1 bottom

axes[0].plot(x, ai, 'r', label='Ai(x)')
axes[1].plot(x, bi, 'b', label='Bi(x)')

for axis in axes:
    axis.set_ylim(-0.5, 1.0)
    axis.set_yticks([])
    axis.legend(loc='upper left')
    axis.axis('off')

axes[1].set_xlim(x.min(), x.max())


# Complex


nx, ny = (2201, 2201)

x = np.linspace(-6.8, 4.8, nx)
y = np.linspace(-8, 8, ny)

xv, yv = np.meshgrid(x, y)

complex_grid = np.zeros(xv.shape, dtype=np.complex_)

complex_grid.real = xv
complex_grid.imag = yv

ai, aip, bi, bip = special.airy(complex_grid)

bi_imag = np.clip(bip.real, -1.3, 2.8)

fig3, ax3 = plt.subplots()
ax3.contourf(xv, yv, bi_imag, levels=20, cmap=colormap)
ax3.contour(xv, yv, bi_imag, levels=20, colors='k',  linestyles='solid')
ax3.axis('off')
ax3.set_position([0, 0, 1, 1])

fig4 = plt.figure()
ax4 = fig4.add_subplot(projection='3d')
ax4.plot_surface(xv, yv, bi_imag, cmap=colormap, linewidth=0, rstride=5,
                 cstride=5)
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

ax4.view_init(elev=84, azim=27, roll=0)

fig3.savefig('/home/josep/Documents/Blocks/docs/chapter-2-special-functions/airy-function/images/airy-bi_imag-contour-highdpi.png',
             format='png', dpi=1200)
fig4.savefig('/home/josep/Documents/Blocks/docs/chapter-2-special-functions/airy-function/images/airy-bi_imag-3dsurf-highdpi.png',
             format='png', dpi=1200)

ai_imag = np.clip(aip.real, -1, 2.5)

fig5, ax5 = plt.subplots()
ax5.contourf(xv, yv, ai_imag, levels=20, cmap=colormap)
ax5.contour(xv, yv, ai_imag, levels=20, colors='k',  linestyles='solid')
ax5.axis('off')
ax5.set_position([0, 0, 1, 1])

fig6 = plt.figure()
ax6 = fig6.add_subplot(projection='3d')
ax6.plot_surface(xv, yv, ai_imag, cmap=colormap, linewidth=0, rstride=5,
                 cstride=5)
ax6.set_position([0, 0, 1, 1])
ax6.xaxis.set_ticklabels([])
ax6.yaxis.set_ticklabels([])
ax6.zaxis.set_ticklabels([])

for line in ax6.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax6.yaxis.get_ticklines():
    line.set_visible(False)
for line in ax6.zaxis.get_ticklines():
    line.set_visible(False)

ax6.view_init(elev=84, azim=9, roll=0)

fig5.savefig('/home/josep/Documents/Blocks/docs/chapter-2-special-functions/airy-function/images/airy-ai_imag-contour-highdpi.png',
             format='png', dpi=1200)
fig6.savefig('/home/josep/Documents/Blocks/docs/chapter-2-special-functions/airy-function/images/airy-ai_imag-3dsurf-highdpi.png',
             format='png', dpi=1200)

    

plt.show()
