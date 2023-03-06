#to display factor

def DisplayFactors(iNo):
    i = 1
    while(i <= (iNo//2)):
        if((iNo%i)==0):
            print(i)
        i = i + 1

def main():
    print("Enter a Number:-")
    iNo = int(input())
    iRet = DisplayFactors(iNo)


if __name__ == "__main__":
    main()
