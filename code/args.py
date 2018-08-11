import sys

def get():
    args = {}
    for i in range(1,len(sys.argv),2):
        args[sys.argv[i]] = sys.argv[i+1]
    return args
