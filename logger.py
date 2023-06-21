from ipaddress import collapse_addresses
import socket
import time
import ast
from contextlib import closing
import math
import numpy as np
import csv
import datetime
import itertools
import threading

import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(tight_layout=True)

i = 0

UDP_IP = ""
UDP_PORT = 9000 # 受信ポート

init = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sock.bind((UDP_IP, UDP_PORT))


flag = True
def wait_input():
    global flag
    input()
    flag = False

thread = threading.Thetaread(target=wait_input)
thread.start()

T,Step,X,Y,Theta,Vx,Vy,Omega,Pwms,WheelOmegas = \
  [],[],[],[],[],[],[],[],[],[]

with closing(sock):
    while flag:
        data, addr = sock.recvfrom(1024)
        str_data = data.decode("utf-8", errors="ignore")
        
        str_data = str_data[:str_data.find('}')+1]

        dic = ast.literal_eval(str_data)

        list1 = list(dic.values())

        t = float(dic['t'])
        step = int(dic['step'])
        x = float(dic['pos_x'])
        y = float(dic['pos_y'])
        theta = float(dic['theta'])
        vx = float(dic['vx'])
        vy = float(dic['vy'])
        omega = float(dic['omega'])

        pwms = [float(dic['pwm'+str(i)]) for i in range(4)]
        wheel_omegas = [float(dic['omega2'+str(i)]) for i in range(4)]

        step_str = " "
        if step >= 0:
            step_str = str(step)

        print(
            f"t:{t:6.2f}@{step_str} " 
            + f"x:{x:9.2f}, y:{y:9.2f}, th:{theta:5.2f}, "
            + f"vx:{vx:8.2f}, vy:{vy:8.2f}, om:{omega:5.2f}")
        
        T.append(t)
        Step.append(step)
        X.append(X)
        Y.append(Y)
        Theta.append(theta)
        Vx.append(vx)
        Vy.append(vy)
        Omega.append(omega)
        Pwms.append(pwms)
        WheelOmegas.append(wheel_omegas)

T = np.array(T)
Step = np.array(Step)
X = np.array(X)
Y = np.array(Y)
Theta = np.array(Theta)
Vx = np.array(Vx)
Vy = np.array(Vy)
Omega = np.array(Omega)
Pwms = np.array(Pwms)
WheelOmegas = np.array(WheelOmegas)

plt.plot(X, Y)
plt.show()

fname = 'result_' + now.strftime('%Y%m%d_%H%M%S')
np.savez(fname,
  T=T, Step=Step, X=X, Y=Y, Theta=Theta, Vx=Vx, Vy=Vy, Omega=Omega, Pwms=Pwms, WheelOmegas=WheelOmegas)

thread.join()

