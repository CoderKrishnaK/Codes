# Parallel programming , Serial Programming

import multiprocessing

def main():
    # This display logical count of cores in our CPU
    print("Number of Cores are:-",multiprocessing.cpu_count())

if __name__ == "__main__":
    main()

