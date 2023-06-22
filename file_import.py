import numpy as np

def load(fname):
    T,X,Y,Theta,Vx,Vy,Omega = [np.zeros((0)) for _ in range(7)]
    Step = np.array([], dtype=int)
    WheelOmegas = np.zeros((0,4))

    for l in open(fname, "r").readlines():
        l = l.rstrip("\n")
        l = l.split()
        if len(l) != 16:
            continue

        wheel_omegas = np.zeros(4)
        t,step, \
            x,y,theta, \
            vx,vy,omega, \
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
        WheelOmegas = np.append(WheelOmegas, np.array([wheel_omegas]), axis=0)

    t = np.array(T)
    step = np.array(Step)
    x = np.array(X)
    y = np.array(Y)
    theta = np.array(Theta)
    vx = np.array(Vx)
    vy = np.array(Vy)
    omega = np.array(Omega)
    wheel_omegas = np.array(WheelOmegas)

    last_wheel_omegas = np.zeros(4)
    wheel_omegas_raw = np.zeros((0,4))
    for w in wheel_omegas:
        tmp = (w - 0.9*last_wheel_omegas) / 0.1
        wheel_omegas_raw = np.append(
            wheel_omegas_raw, np.array([tmp]), axis=0)

    return (
        t, step,
        x, y, theta,
        vx, vy, omega,
        wheel_omegas, wheel_omegas_raw
    )
