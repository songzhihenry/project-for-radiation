import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML


fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2,2,
                                 sharex=False,
                                 sharey=True,
                                  tight_layout=False)
fig.subplots_adjust(hspace=0.5)

ax11.set_xlim((0,60))
ax11.set_ylim((0,10))
ax11.set_xlabel('distance(app)')
ax11.set_ylabel('time')

ax12.set_xlim((0,10))
ax12.set_xlabel(r'$\beta_{app}$')

ax21.set_xlim((0,20))
ax21.set_xlabel('distance')

ax22.set_xlim((0,1.3))
ax22.set_xlabel(r'$\beta$')


t=np.linspace(0,10,1000)
gamma=2
theta=np.pi/10
beta_t=(1-gamma**(-2))**0.5
beta_app_t=beta_t*np.sin(theta)/(1-beta_t*np.cos(theta))
line11, = ax11.plot(beta_app_t*t,t,lw=2)

tt=t*0+1
beta_app=beta_app_t+t*0
line12, = ax12.plot(beta_app,t,lw=2)

beta=beta_t+t*0
line21, = ax21.plot(beta*t,t,lw=2)

line22, =ax22.plot(beta,t,lw=2)


ax11.plot(t,t, label='lightcone edge 1', color='red', linestyle='--')
ax12.plot(tt,t, label='speed of light 1', color='pink', linestyle='--')
ax21.plot(t,t, label='light cone edge 2', color='green', linestyle='--')
ax22.plot(tt,t, label='speed of light 2', color='purple', linestyle='--')

ax11.legend(loc='lower right')
ax12.legend(loc='upper right')
ax21.legend(loc='lower right')
ax22.legend(loc='upper left')

def init():
    line11.set_xdata(0)
    line12.set_xdata(0)
    line21.set_xdata(0)
    line22.set_xdata(0)
    return (line11, line12, line21, line22,)


def animate(i):
    gamma=2
    theta=np.pi*0.01*i
    beta_t=(1-gamma**(-2))**0.5
    beta_app_t=abs(np.sin(theta))*beta_t/(1-beta_t*abs(np.cos(theta)))
    beta_app=beta_app_t+t*0
    beta=beta_t+t*0
    
    line11.set_xdata(beta_app*t)
    line12.set_xdata(beta_app)
    line21.set_xdata(beta*t)
    line22.set_xdata(beta)
    
    ax11.set_title(r'$\theta$='+str(theta))
    ax12.set_title(r'$\beta_{app}$ vs time')
    ax22.set_title(r'$\beta$ vs time')
    ax21.set_title(r'$\beta$='+str(beta_t))
    
    return(line11, line12, line21, line22,)

anim=animation.FuncAnimation(fig=fig, func=animate, init_func=init,
                             frames=500, interval=20,
                             blit=False)


anim.save('fixed beta.mp4')
