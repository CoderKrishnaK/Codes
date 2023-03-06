"""
Automation in Python
12/11/2022

"""
import schedule
import time
import datetime

def Fun():
    print("Current time is :-",datetime.datetime.now())
def main():
    print("Inside Task Schedular")
    print("Current time is :-",datetime.datetime.now())
    print("--------------------------------------------")
    
    schedule.every(1).minutes.do(Fun)

    # uncoditional infinite loop
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()