import time

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even Number :",i)


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd Number :",i)

  
def main():
    print("Demonstration of Serial Programming")
    DisplayEven(2000)
    DisplayOdd(2000)

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