import sys
import bvh

def dp(a,b):
    return abs(a-b)

def dr(a,b):
    if abs(a-b) > 180:
        return 360 - abs(a-b)
    return abs(a-b)

INPUT = sys.argv[1]
bvh_file = bvh.read_file(INPUT)
p = bvh_file["POSITIONS"]
r = bvh_file["ROTATIONS"]
nf = len(p[:,0])

pav = 0;
for c in range(3):
    for f in range(nf-1):
        pav += dp(p[f,c],p[f+1,c]);
pav = pav/(3*(nf))

rav = 0;
for j in range(21):
    for c in range(3):
        for f in range(nf-1):
            rav += dr(r[f,j,c],r[f+1,j,c])
rav = rav/(3*21*(nf-1))

print("rav = " + str(round(rav,2)) + "      pav = " + str(round(pav,2)))
