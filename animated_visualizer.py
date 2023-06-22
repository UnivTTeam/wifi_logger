import numpy as np
import matplotlib.pyplot as plt
import sys
from file_import import load

if len(sys.argv) < 2:
    print("usage: python3 visualize.py [filename]")
    exit()

(
    t, step,
    x, y, theta,
    vx, vy, omega,
    pwms, wheel_omegas, wheel_omegas_raw
) = load(sys.argv[1])

fig, ax = plt.subplots()
scatter = ax.scatter([], [])
X,Y = [],[]

for i in range(len(t)):
    a,b = x[i],y[i]
    X.append(a)
    Y.append(b)
    scatter.set_offsets(list(zip(X, Y)))

    fig.canvas.draw()
    plt.show()

