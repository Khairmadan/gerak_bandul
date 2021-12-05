import math
import modulrumus
import csv
l = float(input("masukkan panjang tali = "))
g = float(input("masukkan percepatan gravitasi = "))
theta = float(input("masukkan sudut simpangan bandul = "))
omega = modulrumus.omega(g=g,l=l)
T = modulrumus.periode(g=g,l=l)
F = modulrumus.frekuensi(T=T)
theta2 = math.radians(theta)
panjanglintasan = modulrumus.panjanglintasan(l=l,teta=theta2)
A = modulrumus.amplitudo(panjanglintasan)
t = 0
data = open("data.csv","w")
tulisdata = csv.writer(data)
teks = ('t','xt','yt','vt','at')
tulisdata.writerow(teks)
Ax = modulrumus.Ax(A=A,theta=theta2)
Ay = modulrumus.Ay(l=l,A=A,theta=theta2)
for i in range(100):
    xt = float(modulrumus.posisix(Ax=Ax,omega=omega,t=t))
    yt = modulrumus.posisiy(Ay=Ay, omega=omega, t=t)
    vt = modulrumus.kecepatan(A=A,omega=omega,t=t)
    at = modulrumus.percepatan(A=A,omega=omega,t=t)
    teks2 = (t,xt,yt,vt,at)
    tulisdata.writerow(teks2)
    t = t + 0.1
