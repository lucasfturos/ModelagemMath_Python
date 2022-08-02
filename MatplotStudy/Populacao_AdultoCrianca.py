import pylab as P

N = [10000]
n0 = 10000
t = 100

r = 0.02
m = 0.03
im = 0
em = 0
ma = 0.01
mc = 0.01
ra = 0.02
e = 0.1
C = [10000]
A = [0]
a0 = 0
c0 = 10000


def Modelo(n0):
    nf = n0 + r * n0 - m * n0 + im - em * n0
    N.append(nf)
    return nf


def Modelo2(c0, a0):
    cf = c0 + ra * a0 - mc * c0 - e * c0
    af = a0 + e * c0 - ma * a0
    C.append(cf)
    A.append(af)
    return cf, af


for i in range(t):
    c0, a0 = Modelo2(c0, a0)
    n0 = Modelo(n0)

P.subplot(121)
P.plot(A, ".", C, "r^")
P.legend(["Adultos", "Crianças"])
P.xlabel("tempo")
P.subplot(122)
P.plot(N, ".")
P.legend(["População"])
P.xlabel("tempo")
P.show()
