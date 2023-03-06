print("Appliaction to demonstrate industrial programming")

def Addition(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def main(): #tu swatha run hou shakte ka ? asked by interpretor
    print("Enter first number : ")
    no1 = int(input())
    print("Enter Second Number : ")
    no2 = int(input())
    
    iRet = Addition(no1,no2)
    print("Addition is: ",iRet)

if __name__ == "__main__":  #in-built word __main__
    main()    



