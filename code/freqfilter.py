import numpy as np
import math

# Returns the Fast Fourier Transform (FFT) of V by
#   using pad of pad_number on each side.
def fft(V,pad_number):
    return np.fft.fft(pad(V,pad_number))

# Returns the Inverse Fast Fourier Transform (IFFT) of F
#   and unpad the result by pad_number on each side.
def ifft(F,pad_number):
    return unpad(np.fft.ifft(F),pad_number)

# Returns the vector which corresponds to the low pass gussian filter
#   with the size t and cutting the p % of highest frequencies.
def gaussian_filter(t, sigma):
    H = np.zeros(t)
    for u in range(int(t/2)):
        H[u] = math.exp(-u**2/(2*sigma))
    for u in range(int(t/2),t):
        H[u] = math.exp(-(t-u)**2/(2*sigma))
    return H

# Returns the vector which corresponds to the low pass butterworth filter
#   with the size t, order n and cutting the p % of highest frequencies. 
def butter_worth_filter(t, u0, n):
    H = np.zeros(t)
    for u in range(int(t/2)):
        H[u] = 1/math.sqrt(1 + (u/u0)**(2*n))
    for u in range(int(t/2),t):
        H[u] = 1/math.sqrt(1 + ((t-u)/u0)**(2*n))
    return H

# Applies the filter_ to the fourier vector by
#   multiplying value by value of the vectors
#   and returns the result.
def apply_filter(fourier, filter_):
    v = np.zeros(len(fourier),dtype=complex)
    for i in range(len(v)):
        v[i] = fourier[i]*filter_[i]
    return v

# Apply pad on the vector.
def pad(V,n):
    vaux = np.array(np.zeros(len(V)+2*n),dtype=type(V))
    vaux[0:n] = V[0]*np.ones(n)
    vaux[n:len(V)+n] = V
    vaux[len(V)+n:len(vaux)] = V[-1]*np.ones(n)
    return vaux

# Remove pad of the vector.
def unpad(V,n):
    return V[n:len(V)-n]
