# Parallel programming , Serial Programming

import os

def main():
    # This display logical count of cores in our CPU
    print("PID of Current process is :-",os.getpid())
    print("PID of Parent process is :-",os.getppid())   #command prompt
    
if __name__ == "__main__":
    main()

