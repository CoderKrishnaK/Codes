# Application to findout the maximum number

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    print("Enter first number")
    Value1 = input()    #Accept and store value in Value1 input function

    print("Enter Second number")
    Value2 = input()

    Ans = Maximum(int(Value1), int(Value2))
    print("Largest Number is: ",Ans)
    

if __name__ == "__main__":
    main()
