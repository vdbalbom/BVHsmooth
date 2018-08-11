import numpy as np

# In this project, the BVH format is a structure which contains these informations:
#       HIERARCHY
#       FRAME NUMBER
#       FRAME TIME
#       DURATION
#       FRAME RATE
#       JOINT NUMBER
#       POSITIONS
#       ROTATIONS
# This python file contains 2 functions:
#       read_file(input)
#           PARAM input (string) - the BVH file path
#           RETURN (map) - the BVH structure
#       write_file(output, bvh)
#           PARAM output (string) - the BVH output file path
#           PARAM bvh (map) - the BVH structure
#           RETURN (void)
# ----------------------------------------------------------------------------------


# PARAM input (string) - the BVH file path
# RETURN (map) - the BVH structure
def read_file(input):
    # open file and get data
    with open(input) as f:
        data = f.readlines()
    # close file
    f.close()
    
    i = 0 # initialize the iterator
    h = "" # hierarchy
    nj = 1 # joints number (starts with one because of the root)
    
    # get the hierarchy and the number of joints
    while("MOTION" not in data[i]):
        if ("JOINT" in data[i]): nj += 1
        h += data[i]
        i += 1

    # get some time parameters
    fn = int(data[i+1].split(' ')[1]) # FRAME NUMBER - number of frames
    ft = float(data[i+2].split(' ')[2]) # FRAME TIME - duration of each frame in seconds
    d = fn*ft # duration in seconds is equal the number of frame times the duration of each frame in seconds
    fps = 1/ft # FRAME RATE
   
    # the line of the bvh file in which starts de motion values (this line corresponds to the first frame)
    i += 3

    # v is the motion values matrix
    v = np.zeros((fn,nj*3 + 3))
    k = 0
    n = len(data)
    while(i < n):
        line = np.array(data[i].split(" "))[0:nj*3 + 3]
        v[k] = line.astype(np.float)
        i += 1
        k += 1
    
    # get the positions matrix (POSITIONS[FRAME, CHANNEL]) - only the root joint has the position channels
    p = v[:,0:3]
    
    # get the rotations matrix (ROTATIONS[FRAME, JOINT, ROTATION CHANNEL])
    r = np.zeros((len(v),nj,3))
    for i in range(nj):
        r[:,i,0] = v[:, i*3 + 3]
        r[:,i,1] = v[:, i*3 + 4]
        r[:,i,2] = v[:, i*3 + 5]
    
    # return the BVH STRUCTURE
    return {"HIERARCHY": h, "FRAME NUMBER": fn, "FRAME TIME": ft, "DURATION": d, "FRAME RATE": fps, "JOINT NUMBER": nj,"POSITIONS": p, "ROTATIONS": r}


# PARAM output (string) - the BVH output file path
# PARAM bvh (map) - the BVH structure
# RETURN (void)
def write_file(output, bvh):
    # (create and) open file
    file = open(output, 'w+')

    # write the hierarchy in the file
    file.write(bvh["HIERARCHY"].replace("\r", ""))

    # write motion information in the file
    file.write("MOTION\n")
    file.write("Frames: " + str(bvh["FRAME NUMBER"]) + "\n")
    file.write("Frame Time: " + str(bvh["FRAME TIME"]) + "\n")

    r = bvh["ROTATIONS"] # get rotations
    p = bvh["POSITIONS"] # get positions
    nj = bvh["JOINT NUMBER"] # get joint number
    
    # construct the motion values matrix
    v = np.zeros((bvh["FRAME NUMBER"],nj*3+3))
    v[:,0:3] = p # add the position information
    # add the rotation information
    for i in range(nj):
        v[:, i*3 + 3] = r[:,i,0]
        v[:, i*3 + 4] = r[:,i,1]
        v[:, i*3 + 5] = r[:,i,2]

    # write the motion values in the file
    for i in range(bvh["FRAME NUMBER"]):
        file.write(" ".join(v[i].astype(str)) + "\n")

    # close file
    file.close()
