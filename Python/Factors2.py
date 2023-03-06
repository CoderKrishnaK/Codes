#to display factor

def main():
    print("Enter a Number:-")
    iNo = int(input())
    iRet = DisplayFactors(iNo)

def DisplayFactors(iNo):
    for i in range(1,(iNo//2+1),1):     #int(iNo/2)+1   time complexity N/2 efficiency
        if((iNo%i)==0):
            print(i)
        #i = i + 1

if __name__ == "__main__":
    main()
