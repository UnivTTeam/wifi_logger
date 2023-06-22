import numpy as np

def load(fname):
    T,X,Y,Theta,Vx,Vy,Omega = [np.zeros((0)) for _ in range(7)]
    Step = np.array([], dtype=int)

    for l in open(fname, "r").readlines():
        l = l.rstrip("\n")
        l = l.split()
        if len(l) != 8:
            continue

        wheel_omegas = np.zeros(4)
        t,step, \
            x,y,theta, \
            vx,vy,omega, \
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

    t = np.array(T)
    step = np.array(Step)
    x = np.array(X)
    y = np.array(Y)
    theta = np.array(Theta)
    vx = np.array(Vx)
    vy = np.array(Vy)
    omega = np.array(Omega)

    return (
        t, step,
        x, y, theta,
        vx, vy, omega,
    )

if __name__ == '__main__':
    load("result_20230623_031519.csv")

