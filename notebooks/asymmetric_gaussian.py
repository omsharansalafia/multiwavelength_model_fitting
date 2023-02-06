import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

def ag(x,x0,sl,sh,fsys):
    s = np.where(x>x0,sh,sl)
    p = np.exp(-0.5*((x-x0)/(s**2+fsys**2*x0**2)**0.5)**2)
    norm = 0.5*(np.sqrt(2*np.pi*(sl**2+fsys**2*x0**2))+np.sqrt(2*np.pi*(sh**2+fsys**2*x0**2)))
    return p/norm

t = np.linspace(0,10,100)
x = np.linspace(-10.,10.,1000)
x0 = 1.
sl = 0.1
sh = 0.5
fsys = 0.001

plt.plot(x,ag(x,x0,sl,sh,fsys))
plt.show()


def init():
    ax.set_xlim(-3., 4)
    ax.set_ylim(-0.1, 1.5)
    return ln,


## make animation ###
fig = plt.figure()
ax = plt.axes([0.1,0.3,0.85,0.65])

plt.xlabel(r'$F$')
plt.ylabel(r'$p(\vec d_i\,|\,F)$')

ln, = plt.plot(x,ag(x,x0,sl,sh,fsys), ls='-',color='r')


# reference axes
plt.axvline(x=x0,ls=':',color='gray',zorder=-10)


plt.tick_params(which='both',direction='in',top=True,right=True)

axsl = plt.axes([0.2, 0.05, 0.65, 0.03])
sl_slider = Slider(
    ax=axsl,
    label=r'$\sigma_\mathrm{l}$',
    valmin=0.1,
    valmax=10.,
    valinit=0.1,
)

axsh = plt.axes([0.2, 0.085, 0.65, 0.03])
sh_slider = Slider(
    ax=axsh,
    label=r'$\sigma_\mathrm{h}$',
    valmin=0.1,
    valmax=1.,
    valinit=0.5,
)

axfsys = plt.axes([0.2, 0.12, 0.65, 0.03])
fsys_slider = Slider(
    ax=axfsys,
    label=r'$f_\mathrm{sys}$',
    valmin=0.00001,
    valmax=1.,
    valinit=0.001,
)

#axph.add_artist(axph.xaxis)
#plt.xticks(np.arange(0.,2.,0.25)*np.pi,[r'$0$',r'$\pi/4$',r'$\pi/2$',r'$3\pi/4$',r'$\pi$',r'$5\pi/4$',r'$3\pi/2$',r'$7\pi/4$'])
#plt.tick_params(which='both',direction='in',top=True,bottom=False,labelbottom=False,labeltop=True)

def update(i):
    sl = sl_slider.val
    sh = sh_slider.val
    fsys = fsys_slider.val
    
    ln.set_data(x, ag(x,x0,sl,sh,fsys))
    return ln,


ani = FuncAnimation(fig, update, frames=np.arange(len(t)),
                    init_func=init, blit=False, interval=100)

plt.tick_params(which='both',direction='in',top=True,right=True)

plt.show()

