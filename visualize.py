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
) = load(sys.argv[1])
n = max(step)+1

if True:
    plt.gca().set_aspect('equal')
    plt.xlim([-6500, 500])
    plt.ylim([-500, 6500])
    for i in range(0, n):
        plt.plot(x[step==i], y[step==i])
    plt.show()

if False:
    fig = plt.figure()
    v = np.array([vx, vy, omega]).T
    for w in range(3):
        ax = fig.add_subplot(3, 1, w+1)
        for i in range(0, n):
            ax.plot(t[step==i], v[step==i, w])
    plt.show()
