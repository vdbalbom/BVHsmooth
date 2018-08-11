import numpy as np

def apply_border(v, M):
    ini = v[0]*np.ones(int(M/2), dtype=v.dtype)
    fi = v[-1]*np.ones(int(M/2), dtype=v.dtype)
    return np.concatenate((ini,v,fi), axis=0)

def remove_border(v,M):
    return v[int(M/2):-int(M/2)]

def apply_average(v, M):
    v = apply_border(v,M)
    for i in range(int(M/2),len(v)-int(M/2)):
        aux = 0
        for j in range(i-int(M/2),i+int(M/2)+1):
            aux += v[j]
        v[i] = aux/M
    return remove_border(v,M)

