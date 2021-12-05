import math
def omega(g,l):
    omega = math.sqrt(l/g)
    return omega

def periode(g,l):
    omega  = math.sqrt(l/g)
    pi = math.pi
    T = 2 *  pi * omega
    return T
def frekuensi(T):
    F = 1/T
    return F
def panjanglintasan(l ,teta):
    panjang = l * teta
    return panjang
def amplitudo(panjang):
    A = 0.5 * panjang
    return A
def Ax(A,theta):
    Ax = A * math.sin(theta)
    return Ax
def Ay(l,A,theta):
    Ay = l-(A * math.cos(theta))
    return Ay
def posisix(Ax,omega,t):
    xt = Ax * math.cos(omega * t )
    return xt
def kecepatan(A,omega,t):
    vt = -A * omega  * math.sin(omega * t)
    return vt
def percepatan(A, omega, t):
    at = -A * (omega**2) * math.sin(omega * t)
    return at
def posisiy(Ay,omega,t):
    yt = Ay * math.sin(omega*t)
    return yt
