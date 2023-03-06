# to check even or not

def CheckEven(No):
    if((No%2)==0):
        return True
    else:
        return False

def CheckEvenX(No):
    return (No % 2 == 0)

def main():
    print("Enter a Number:-")
    iValue = int(input())

    """Ans = CheckEven(iValue)
    if(Ans == True):
        print("Its Even")
    else:
        print("Its Odd") 
    """
    Ans = CheckEvenX(iValue)
    if(Ans == True):
        print("Its Even")
    else:
        print("Its Odd") 
    

if __name__ == "__main__":
    main()