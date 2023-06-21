import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print("usage: python3 visualize.py [filename]")

fname = sys.argv[1]
T,X,Y,Theta,Vx,Vy,Omega = [np.zeros((0)) for _ in range(7)]
Step = np.array([], dtype=int)
Pwms,WheelOmegas = [np.zeros((0,4)) for _ in range(2)]

for l in open(fname, "r").readlines():
    l = l.rstrip("\n")
    l = l.split()
    if len(l) != 16:
        continue

    pwms = [0,0,0,0]
    wheel_omegas = [0,0,0,0]
    t,step, \
        x,y,theta, \
        vx,vy,omega, \
        pwms[0],pwms[1],pwms[2],pwms[3], \
        wheel_omegas[0],wheel_omegas[1],wheel_omegas[2],wheel_omegas[3] \
        = map(float, l)
    step = int(step)

    T = np.append(T, t)
    Step = np.append(Step, step)
    X = np.append(X, x)
    Y = np.append(Y, y)
    Theta = np.append(Theta, theta)
    Vx = np.append(Vx, vx)
    Vy = np.append(Vy, vy)
    Omega = np.append(Omega, omega)
    Pwms = np.append(Pwms, pwms)
    WheelOmegas = np.append(WheelOmegas, wheel_omegas)

t = np.array(T)
step = np.array(Step)
x = np.array(X)
y = np.array(Y)
theta = np.array(Theta)
vx = np.array(Vx)
vy = np.array(Vy)
omega = np.array(Omega)
pwms = np.array(Pwms)
wheel_omegas = np.array(WheelOmegas)

for i in range(0, max(Step)+1):
    plt.plot(x[i==step], y[i==step])
plt.show()
