import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
from matplotlib import style
from math import sin

style.use('fivethirtyeight')

data = [0,0,0,0,0,0,0,0,0,0]
xs = range(len(data))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def update(i):
    ax1.clear()
    ax1.plot(xs, data)
    data.remove(data[0])
    #nv = random.randrange(10)
    nv = sin(i)
    data.append(nv)
    print(nv, end=',')
    #input()
ani = animation.FuncAnimation(fig, update, interval=10)
#plt.axis([0,9,0,9])
plt.show()
