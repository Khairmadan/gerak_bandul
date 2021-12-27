import math
def omega(g,l):
    a = g/l
    omega = math.sqrt(a)
    return omega

def periode(g,l):
    a = g/l
    omega  = math.sqrt(1/a)
    pi = math.pi
    T = 2 *  pi * omega
    return T
def frekuensi(T):
    F = 1/T
    return F
def panjanglintasan(l ,teta):
    panjang = 2*l * teta
    return panjang
def amplitudo(panjang):
    A = 0.5 * panjang
    return A
def Ax(A,theta):
    Ax = A * math.sin(theta)
    return Ax
def Ay(l,A,theta):
    Ay = (l * math.cos(theta))
    return Ay
def posisix(Ax,omega,t):
    xt = Ax * math.cos(omega * t )
    return xt
def kecepatan(A,omega,t):
    vt = -A * omega  * math.sin(omega * t)
    return vt
def percepatan(A, omega, t):
    at = -A * (omega**2) * math.cos(omega * t)
    return at
def posisiy(xt,l):
    yt = - math.sqrt((l**2)-(xt**2))
    return yt
