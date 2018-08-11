import numpy as np
import math

def aprox(x):
    a = round(x.real,8)
    b = round(x.imag,8)
    if b == 0:
        return a
    return(a + b*1j)

class degree(float):
    def __init__(self,x):
        self = self
        self.p = polar(aprox(math.cos((x*math.pi)/180) + math.sin((x*math.pi)/180)*1j))
        pass
    def to_polar(self):
        return self.p

class polar(complex):
    def __init__(self,x):
        pass
    def to_degree(self):
        return degree(aprox((math.atan2(self.imag,self.real)*180)/math.pi))

def floats_to_degrees(V):
    D = np.zeros(len(V), dtype=degree)
    for i in range(len(D)):
        D[i] = degree(V[i])
    return D

def polars_to_degrees(V):
    D = np.zeros(len(V), dtype=degree)
    for i in range(len(D)):
        D[i] = V[i].to_degree()
    return D

def complexes_to_polars(V):
    P = np.zeros(len(V), dtype=polar)
    for i in range(len(P)):
        P[i] = polar(V[i])
    return P

def degrees_to_polars(V):
    P = np.zeros(len(V), dtype=polar)
    for i in range(len(P)):
        P[i] = V[i].to_polar()
    return P
