# Creating two seperate process as Even and Odd 
# p1 and p2 are process handle for the process
import time
import multiprocessing

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even Number :",i)


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd Number :",i)

  
def main():
    print("Demonstration of Parallel Programming using multiple Processes")
    Number = 200
    
    p1 = multiprocessing.Process(target = DisplayEven,args = (Number,))
    p2 = multiprocessing.Process(target = DisplayOdd,args = (Number,))
    
    p1.start()  #only starts process does not execute
    p2.start()

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