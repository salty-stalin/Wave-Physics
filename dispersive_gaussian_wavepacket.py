
import numpy as np
import matplotlib.pyplot as plt
print(np.exp((-1*2**2)))
c=1
h=1
m=1
pi=3.1415926535897932384626433
def wave_real(x,t,omega,k):
    return (((2/pi)**(1/4))/(1+4*(h**2)*(t**2)/m**2))*np.exp((-x**2)/(1+4*(h**2)*(t**2)/m**2))*(np.cos((2*(x**2)*h*t)/(1+4*(h**2)*(t**2)/m**2))*(1+(5*(h**2)*(t**2))/2*(m**2)-((h**4)*(t**4)/m**4))+np.sin((2*(x**2)*h*t)/(1+4*(h**2)*(t**2)/m**2))*((h*t)/m + 3*(h**3)*(t**3)/2*(m**3)))

def wave_imaginary(x,t,omega,k):
    return (((2/pi)**(1/4))/(1+4*(h**2)*(t**2)/m**2))*np.exp((-x**2)/(1+4*(h**2)*(t**2)/m**2))*(np.cos((2*(x**2)*h*t)/(1+4*(h**2)*(t**2)/m**2))*((h*t)/m - 3*(h**3)*(t**3)/2*(m**3)) +np.sin((2*(x**2)*h*t)/(1+4*(h**2)*(t**2)/m**2))*(1+(5*(h**2)*(t**2))/2*(m**2)-((h**4)*(t**4)/m**4)))


xx=np.arange(0,30,.01)
xxx=np.flip(xx,0)
print(xx)
k0=10
k1=8
omega0=40
omega1=20
print(omega0)

for t in np.arange(0,30,.02):
    plt.title('$t=$'+str(t))
    plt.subplot(311)
    aa=plt.plot(xx,wave_real(xx,t,omega0,k0))
    plt.ylabel('$\\psi$',fontsize=15)
    plt.subplot(312)
    aa=plt.plot(xx,wave_imaginary(xx,t,omega0,k0))
    plt.ylabel('$\\psi_*$',fontsize=15)
    plt.subplot(313)
    aa=plt.plot(xx,wave_real(xx,t,omega0,k0)**2+wave_imaginary(xx,t,omega0,k0)**2)
#    aa=plt.plot(xx,2*wave(xx,t,(omega0-omega1)/2.,(k0-k1)/2.),'r')
#    aa=plt.plot(xx,-2*wave(xx,t,(omega0-omega1)/2.,(k0-k1)/2.),'r')
    plt.ylabel('$|\\psi|^2$',fontsize=15)
    plt.xlabel('x')
    plt.pause(.0000001)

    plt.clf()
   