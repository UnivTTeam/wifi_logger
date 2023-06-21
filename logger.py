from ipaddress import collapse_addresses
import socket
import ast
from contextlib import closing
import numpy as np
import datetime

import matplotlib.pyplot as plt

UDP_IP = ""
UDP_PORT = 9000 # 受信ポート

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sock.bind((UDP_IP, UDP_PORT))

now = datetime.datetime.now()
fname = 'result_' + now.strftime('%Y%m%d_%H%M%S') + ".csv"
ofile = open(fname, 'w')

with closing(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            str_data = data.decode("utf-8", errors="ignore")
            
            str_data = str_data[:str_data.find('}')+1]

            dic = ast.literal_eval(str_data)

            list1 = list(dic.values())

            t = float(dic['t'])
            step = int(dic['s'])
            x = float(dic['x'])
            y = float(dic['y'])
            theta = float(dic['th'])
            vx = float(dic['vx'])
            vy = float(dic['vy'])
            omega = float(dic['om'])
            pwms = [float(dic['p'+str(i)]) for i in range(4)]
            wheel_omegas = [float(dic['om'+str(i)]) for i in range(4)]

            step_str = "  "
            if step >= 0:
                step_str = "@"+str(step)

            print(
                f"t:{t:6.2f}{step_str} " 
                + f"x:{x:9.2f}, y:{y:9.2f}, th:{theta:7.4f}, "
                + f"vx:{vx:8.2f}, vy:{vy:8.2f}, om:{omega:7.4f}"
            )

            print(
                t,step,
                x,y,theta,
                vx,vy,omega,
                pwms[0],pwms[1],pwms[2],pwms[3],
                wheel_omegas[0],wheel_omegas[1],wheel_omegas[2],wheel_omegas[3],
                file=ofile
            )

        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            break
        except Exception as e:
            print("[Unknown Error]")
            print(e)

print("save log...")


