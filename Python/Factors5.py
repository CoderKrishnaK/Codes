#to display factor

#import NumberModule                            generalized import
#from NumberModule import DisplayFactors        Specified import
#from NumberModule import *
import NumberModule as NUM                      # Aliazed import

def main():
    print("Enter a Number:-")
    iNo = int(input())
    iRet = NUM.DisplayFactors(iNo)


if __name__ == "__main__":
    main()
