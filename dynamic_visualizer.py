import matplotlib.pyplot as plt
import queue
import threading
import time
import numpy as np
import sys

from file_import import load

if len(sys.argv) < 2:
    print("usage: python3 visualize.py [filename]")
    exit()

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

class Visualizer:
    def __init__(self):
        # グラフの設定
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim([-6500, 500])
        self.ax.set_ylim([-500, 6500])
        plt.gca().set_aspect('equal')

        # データ保存
        self.X = []
        self.Y = []
        self.c = []

        self.q = queue.Queue()


        # グラフを描画して表示
        plt.show(block=False)
    
    def append(self, x, y, i):
        self.q.put((x,y,i))

    def update(self, t):
        while self.q.qsize() > 0:
            x,y,i = self.q.get()
            c = colors[i]

            # データ追加
            self.X.append(x)
            self.Y.append(y)
            self.c.append(c)
            self.ax.scatter([x], [y], c=c, s=4)

        # 再描画
        plt.draw()
        plt.pause(t)

    def run(self, t):
        while True:
            self.update(t)

if __name__ == '__main__':
    (
        t, step,
        x, y, theta,
        vx, vy, omega,
    ) = load(sys.argv[1])
    v = Visualizer()

    def data_loader():
        global v
        for X,Y,S in zip(x[step>=0], y[step>=0], step[step>=0]):
            v.append(X, Y, S)
            time.sleep(0.02)
    thread = threading.Thread(target=data_loader)
    thread.start()

    v.run(0.1)

