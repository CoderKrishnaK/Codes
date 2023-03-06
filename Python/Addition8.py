print("Appliaction to demonstrate industrial programming")

import MarvellousModule

def main(): #tu swatha run hou shakte ka ? asked by interpretor
    print("Value of __name__ from main is: ",__name__)

    print("Enter first number : ")
    no1 = int(input())
    print("Enter Second Number : ")
    no2 = int(input())
    
    iRet = MarvellousModule.Addition(no1,no2)
    print("Addition is: ",iRet)

if __name__ == "__main__":  #in-built word __main__
    main()    



