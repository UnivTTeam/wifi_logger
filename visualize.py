import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import sys
from file_import import load

from odometry import get_odom_param

def Rot(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c,-s,],[s,c]])

if len(sys.argv) < 2:
    print("usage: python3 visualize.py [filename]")
    exit()

(
    t, step,
    x, y, theta,
    vx, vy, omega,
    wheel_omegas, wheel_omegas_raw
) = load(sys.argv[1])
n = max(step)+1

if False:
    for i in range(0, n):
        plt.plot(x[step==i], y[step==i])
    plt.show()

if False:
    fig = plt.figure()
    for w in range(4):
        ax = fig.add_subplot(4, 1, w+1)
        for i in range(0, n):
            ax.plot(t[step==i], wheel_omegas_raw[step==i, w])
    plt.show()

if False:
    fig = plt.figure()
    v = np.array([vx, vy]).T
    for w in range(2):
        ax = fig.add_subplot(4, 1, w+1)
        for i in range(0, n):
            ax.plot(t[step==i], v[step==i, w])
    plt.show()

if True:
    r = np.zeros(2)
    A = get_odom_param()[:,:2]
    Ainv = LA.pinv(A)
    R = []
    for i in range(len(t)):
        v = (Ainv@wheel_omegas[i])[:2]
        r += Rot(theta[i])@v
        R.append(np.array(r))
    a,b = np.array(R).T
    for i in range(0, n):
        plt.plot(a[step==i], b[step==i])
    plt.show()

