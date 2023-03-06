#to display factor

def main():
    print("Enter a Number:-")
    iNo = int(input())
    iRet = DisplayFactors(iNo)

def DisplayFactors(iNo):
    for i in range(1,iNo,1):
        if((iNo%i)==0):
            print(i)
        #i = i + 1

if __name__ == "__main__":
    main()
