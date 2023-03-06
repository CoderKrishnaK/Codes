from sys import *


def Script_Task(No):
    if(No % 2 == 0):
        print("It is Even Number")
    else:
        print("It is Odd Number")

def main():
    print("-----------MARVELLOUS INFOSYSTEMS AUTOMATION---------")
    print("Automation Script Started with name :",argv[0])  

    if(len(argv)!= 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the scripts")
        exit()

    if(argv[1] == "-h"):
        print("Help : This Script is Used to Perform :-_______________")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This Script is Used to Perform :-_______________")
        exit()

    elif((argv[1]== "-u") or (argv[1]== "-U")):
        print("Usage : Provide _____Number of Argument as")
        print("First Argument as : _______")
        print("Second Argument as : _______")
        exit()

    else:
        Script_Task(int(argv[1]))


if __name__ == "__main__":
    main()