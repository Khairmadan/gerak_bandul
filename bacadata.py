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
xii = []
yii = []
for i in range(1000):
    xi.append(x[i])
    yi.append(y[i])
    xii.append(l+1)
    yii.append(0)
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(autoscale_on=False,  xlim=(-l,l), ylim=(-1.1*l,0.1*l))
ax.set_aspect('equal')
ax.grid()
line, = ax.plot([], [], 'o-', lw=1, color="green")
line2, = ax.plot([], [], 'o-', lw=1, color="black")
circle = plt.Circle((xi[1],yi[1]),0.5, color="green")

def animate(i):
    thisx=[0,xi[i]]
    thisy=[0,yi[i]]
    line.set_data(thisx,thisy)
    thisxx =[-l-1,xii[i]]
    thisyy = [0,yii[i]]
    circle.center = xi[i],yi[i]
    line2.set_data(thisxx,thisyy)
    artisline = ax.add_artist(line)
    artistcircle = ax.add_artist(circle)
    artisline2 = ax.add_artist(line2)
    plt.title("t= %0.2f" % t[i]+" s "+", vt = %0.2f"  %vt[i] +" m/s" + ", at = %0.2f" %at[i] + " m/s²")
    return artisline,artisline2, artistcircle
ani = animation.FuncAnimation(fig,animate,frames=900,interval=0.1,blit=False)
plt.show()

