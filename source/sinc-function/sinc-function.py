import numpy as np
import matplotlib.pyplot as plt


plotting_half_window = 8*np.pi

plot_components = True
plot_sum = False

x = np.linspace(-plotting_half_window, plotting_half_window, 10000)
y1 = np.sinc(x / np.pi)

# let's plot the sinc function

fig0, ax0 = plt.subplots()
ax0.set_xlim(left=-plotting_half_window, right=plotting_half_window)
ax0.axis('off')

if plot_sum:
    ax0.plot(x, y1, linestyle=':', color='k')
else:
    ax0.plot(x, y1)


# first we would like to offset by the argument of minimum
sinc_min_index = y1.argmin()
print("First minimum of sinc(x) is x = "+str(x[sinc_min_index]))
offset_value = 2*x[sinc_min_index]

y2 = np.sinc((x+offset_value) / np.pi)
y3 = np.sinc((x-offset_value) / np.pi)
y4 = y1 + y2 + y3

fig, ax = plt.subplots()
ax.set_xlim(left=-plotting_half_window, right=plotting_half_window)
ax.axis('off')

if plot_components:
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.plot(x, y3)

if plot_sum:
    ax.plot(x, y4, color='k', linestyle=':')

#ax.axhline(0, color='k', linestyle=':')
#ax.axvline(-np.pi, color='k')
#ax.axvline(np.pi, color='k')


# next we would like to try offsetting by the pulse width of sinc, 
y2 = np.sinc((x-np.pi)/np.pi)
y3 = np.sinc((x+np.pi)/np.pi)
y4 = y1 + y2 + y3;

fig2, ax2 = plt.subplots()
ax2.set_xlim(left=-plotting_half_window, right=plotting_half_window)
ax2.axis('off')

if plot_components:
    ax2.plot(x, y1)
    ax2.plot(x, y2)
    ax2.plot(x, y3)

if plot_sum:
    ax2.plot(x, y4, color='k', linestyle=':')





plt.show()
