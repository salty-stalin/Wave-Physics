
import numpy as np
import matplotlib.pyplot as plt
print(np.exp((-1*2**2)))
c=1
def wave_real(x,t,omega,k):
    return np.exp(-(x-t)**2)*np.cos(k*x-omega*t)

def wave_imaginary(x,t,omega,k):
    return np.exp(-(x-t)**2)*np.sin(k*x-omega*t)


xx=np.arange(0,10,.01)
xxx=np.flip(xx,0)
print(xx)
k0=10
k1=8
omega0=-40
omega1=20
print(omega0)

for t in np.arange(0,10,.02):
    plt.title('$t=$'+str(t))
    plt.subplot(311)
    sum_real=wave_real(xx,t,omega0,k0)+wave_real(xxx,t,-omega0,k0)
    sum_imaginary=wave_imaginary(xx,t,omega0,k0)+wave_imaginary(xxx,t,-omega0,k0)
    aa=plt.plot(xx,sum_real)
    plt.ylabel('$\\psi$',fontsize=15)
    plt.subplot(312)
    aa=plt.plot(xx,sum_imaginary)
    plt.ylabel('$\\psi_*$',fontsize=15)
    plt.subplot(313)
    aa=plt.plot(xx,sum_real**2+sum_imaginary**2)
#    aa=plt.plot(xx,2*wave(xx,t,(omega0-omega1)/2.,(k0-k1)/2.),'r')
#    aa=plt.plot(xx,-2*wave(xx,t,(omega0-omega1)/2.,(k0-k1)/2.),'r')
    plt.ylabel('$|\\psi|^2$',fontsize=15)
    plt.xlabel('x')
    plt.pause(.0000001)

    plt.clf()
   