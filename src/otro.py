
from numpy import exp,power,pi,sum


def estimador(lam,x0,datos,dimension=1):
    y_est=0
    n=len(datos)
    M=1/(n*power((2*lam**2*pi),dimension/2))
    suma=0
    for xi in datos:
        suma+=gaussDist(xi,x0,lam)
    return M*suma


def gaussDist(xi,x0,l):
    return exp((-0.5)*((xi-x0)/l)**2)