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

s = -1
r = np.zeros(2)

for i in range(len(step)):
    if step[i] != s:
        R = np.array([x[i], y[i]])
        print(s, R - r)
        s = step[i]
        r = np.array(R)
