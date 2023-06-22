from ipaddress import collapse_addresses
import socket
import ast
from contextlib import closing
import numpy as np
import datetime

import matplotlib.pyplot as plt

class Logger:
    def __init__(self):
        UDP_IP = ""
        UDP_PORT = 9000 # 受信ポート

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind((UDP_IP, UDP_PORT))

        now = datetime.datetime.now()
        fname = 'result_' + now.strftime('%Y%m%d_%H%M%S') + ".csv"
        self.ofile = open(fname, 'w')

        self.continue_flag = True

    def callback(self, x, y, step):
        pass

    def start(self):
        with closing(self.sock):
            while self.continue_flag:
                try:
                    data, addr = self.sock.recvfrom(1024)
                    str_data = data.decode("utf-8", errors="ignore")
                    
                    str_data = str_data[:str_data.find('}')+1]

                    dic = ast.literal_eval(str_data)

                    list1 = list(dic.values())

                    t = float(dic['t'])
                    step = int(dic['step'])
                    x = float(dic['x'])
                    y = float(dic['y'])
                    theta = float(dic['theta'])
                    vx = float(dic['vx'])
                    vy = float(dic['vy'])
                    omega = float(dic['omega'])
                    self.callback(x, y, step)

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
                        file=self.ofile
                    )
                except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    break
                except Exception as e:
                    print("[Unknown Error]")
                    print(e)
                    continue

if __name__ == '__main__':
    logger = Logger()
    logger.start()

