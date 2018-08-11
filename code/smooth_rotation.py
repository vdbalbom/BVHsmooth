import numpy as np
import sys
import bvh
import freqfilter
import angle
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

for j in range(len(bvh_file["ROTATIONS"][0,:,0])):
    for i in range(3):
        v = angle.floats_to_degrees(bvh_file["ROTATIONS"][:,j,i])
        p = angle.degrees_to_polars(v)
        if FILTER == "average": f_filtered = spacefilter.apply_average(p, M)
        else:
            f = freqfilter.fft(p,BORDER)
            if FILTER == "gaussian": fil = freqfilter.gaussian_filter(len(f), SIGMA)
            if FILTER == "butterworth": fil = freqfilter.butter_worth_filter(len(f), U0, ORDER)
            f_filtered = freqfilter.apply_filter(f,fil)
            f_filtered = freqfilter.ifft(f_filtered,BORDER)
        p = angle.complexes_to_polars(f_filtered)
        nv = angle.polars_to_degrees(p)
        bvh_file["ROTATIONS"][:,j,i] = nv

bvh.write_file(OUTPUT, bvh_file)
