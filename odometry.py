import numpy as np

from libtf import add_frame, inv_frame


def e(n, i):
    x = np.zeros(n)
    x[i] = 1
    return x

def get_wheel_vel_per_vel(frame):
    vx = e(6, 3)
    vy = e(6, 4)
    vw = e(6, 5)

    l = []
    for v in [vx, vy, vw]:
        static_wheel_to_dynamic_wheel = add_frame(
            inv_frame(frame),
            add_frame(v, frame)
        )
        l.append(static_wheel_to_dynamic_wheel[3])
    return np.array(l)

def get_odom_param():
    wheel_frames = [
        [ 299.81,  289.71, 0.75 * np.pi],
        [-299.81,  289.71,-0.75 * np.pi],
        [-299.81, -289.71,-0.25 * np.pi],
        [ 299.81, -289.71, 0.25 * np.pi],
    ]
    wheel_radius = 51.0

    A = np.array([get_wheel_vel_per_vel(w) for w in wheel_frames]) / wheel_radius
    return A
