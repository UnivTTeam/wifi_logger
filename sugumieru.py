from dynamic_visualizer import Visualizer
from logger import Logger

v = Visualizer()

l = Logger()
l.callback = v.append
l.start()

v.run(0.2)

