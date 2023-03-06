#to display factor

def main():
    print("Enter a Number:-")
    iNo = int(input())
    iRet = DisplayFactors(iNo)

def DisplayFactors(iNo):
    i = 1
    while(i <= (iNo//2)):
        if((iNo%i)==0):
            print(i)
        i = i + 1

if __name__ == "__main__":
    main()
