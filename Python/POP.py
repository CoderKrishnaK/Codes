

def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def main():
    print("Enter First number")
    No1 = int(input())

    print("Enter Second number")
    No2 = int(input())

    iRet = Add(No1,No2)
    print("Adddition is :",iRet)

    Ans = Sub(No1,No2)
    print("Substraction is: ",Ans)

if __name__ == "__main__":
    main()