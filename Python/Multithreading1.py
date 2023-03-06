import time
import threading

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even Number :",i)


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd Number :",i)


def main():
    print("Demonstration of Parallel Programming using multiple Threads")
    Number = 2000
    # keyword argument with variable number of argument
    
    p1 = threading.Thread(target = DisplayEven,args = (Number,))
    p2 = threading.Thread(target = DisplayOdd,args = (Number,))
    
    p1.start()  #only starts process does not execute
    p2.start()

    p1.join()   #control wait until line 30 till upper execution of join() completes
    p2.join()

    print("End of Main")
# how to calculate execution time
# khali method ahe bg 
if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is :-",end_time - start_time)

"""
Factors for time required for process execution
Ram kiti ahe urlrli
Microprocessor speed
O.S. switching 

"""