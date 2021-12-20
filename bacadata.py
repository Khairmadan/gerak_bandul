import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.animation as animation
l = 10
df = pd.read_csv('data.csv')
t = df["t"]
x = df["xt"]
y = df["yt"]
vt = df["vt"]
at = df["at"]
xi = []

yi = []
for i in range(1000):
    xi.append(x[i])
    yi.append(y[i])
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(autoscale_on=False,xlim=(-l,l),ylim=(-1.1*l,0.1*l))
ax.set_aspect('equal')
ax.grid()
line, = ax.plot([],[],'o-',lw=1)

def animate(i):
    thisx=[0,xi[i]]
    thisy=[0,yi[i]]

    line.set_data(thisx,thisy)
    artisline = ax.add_artist(line)
   # circle = plt.Circle((xi[i],yi[i]),0.5)
   # artiscircle = ax.add_artist(circle)
    plt.title("t= %0.2f" % t[i])
    plt.pause(0.01)
  #  circle.remove()

    return artisline , #artiscircle
ani = animation.FuncAnimation(fig,animate,frames=900,interval=0.1,blit=False)
#ani.save(filename="madan.mp4")
plt.show()