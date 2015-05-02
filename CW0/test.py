import numpy as np
import math
from scipy import integrate
import matplotlib.pyplot as plt

def deriv(y, t) :
    yprime = np.array([y[0]**2 - 3*y[0] + np.exp(-t)])
    return yprime

if __name__ == "__main__" :
    time = np.arange(0, 3, 0.01)
    y0 = np.array([0])
    y = integrate.odeint(deriv, y0, time)
    plt.plot(time,y[:,0])
    plt.show()

    # DT = 0.01
    time = np.arange(0, 3, 0.01)
    y = integrate.odeint(deriv, y0, time)
    plt.plot(time,y[:,0])
    # DT = 0.1
    time = np.arange(0, 3, 0.1)
    y = integrate.odeint(deriv, y0, time)
    plt.plot(time,y[:,0])
    # DT = 0.5
    time = np.arange(0, 3, 0.5)
    y = integrate.odeint(deriv, y0, time)
    plt.plot(time,y[:,0])
    # DT = 1
    time = np.arange(0, 3, 1)
    y = integrate.odeint(deriv, y0, time)
    plt.plot(time,y[:,0])

    plt.show()
