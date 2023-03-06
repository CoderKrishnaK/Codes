#command Line input second way of input
from sys import *

def main():
    print("Total number of argument are:-",len(argv))

    print("Name of Application:-",argv[0])
    
    print("First argument:-",argv[1])
    print("Second argument:-",argv[2])
    print("Third argument:-",argv[3])
if __name__ == "__main__":
    main()
