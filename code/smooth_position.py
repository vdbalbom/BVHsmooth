import numpy as np
import freqfilter
import bvh
import sys
import args
import spacefilter

ARGS = args.get()
INPUT = ARGS["-i"]
OUTPUT = ARGS["-o"]
FILTER = ARGS["--filter"]
if FILTER == "butterworth":
    ORDER = int(ARGS["--order"])
    U0 = int(ARGS["--u0"])
    BORDER = int(ARGS["--border"])
if FILTER == "gaussian":
    SIGMA = int(ARGS["--sigma"])
    BORDER = int(ARGS["--border"])
if FILTER == "average":
    M = int(ARGS["-m"])

bvh_file = bvh.read_file(INPUT)

for i in range(0, 3):
    v = bvh_file["POSITIONS"][:,i]
    if FILTER == "average": bvh_file["POSITIONS"][:,i] = spacefilter.apply_average(v,M)
    else:
        f = freqfilter.fft(v,BORDER)
        if FILTER == "gaussian": fil = freqfilter.gaussian_filter(len(f),SIGMA)
        if FILTER == "butterworth": fil = freqfilter.butter_worth_filter(len(f),U0,ORDER)
        ff = freqfilter.apply_filter(f,fil)
        iff = freqfilter.ifft(ff,BORDER)
        bvh_file["POSITIONS"][:,i] = np.real(iff)

bvh.write_file(OUTPUT,bvh_file)
