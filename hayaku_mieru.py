import sys
import time

from dynamic_visualizer import Visualizer

if len(sys.argv) < 2:
    print("usage: python3 visualize.py [filename]")
    exit()

n = 0
def load(fname):
    global n
    ret = []
    for l in open(fname, 'r').readlines()[n:]:
        l = l.rstrip("\n")
        l = l.split()
        if len(l) != 8:
            continue

        step = int(l[1])
        x = float(l[2])
        y = float(l[3])
        ret.append((x, y, step))
        n += 1
    
    return ret

v = Visualizer()

while True:
    v.update(0.1)
    for x,y,step in load(sys.argv[1]):
        v.append(x,y,step)

