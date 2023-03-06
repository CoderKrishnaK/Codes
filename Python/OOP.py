# OOP in python
#Accept 2 numbers and perform addition and subtraction of it

# class = characteristic + Behaviour
# class = Data + Functions

class Arithematic:
    #init method or Contructor Defination
    def __init__(self,A,B):
        self.No1 = A    #instance variable
        self.No2 = B
    #Instance Method
    def Add(self):
        return self.No1 + self.No2


    def Sub(self):
        return self.No1 - self.No2

def main():
    print("Enter First number")
    Value1 = int(input())

    print("Enter Second number")
    Value2 = int(input())

    obj = Arithematic(Value1,Value2)     #object creation   #parameterized contructor

    Ans = obj.Add()
    print("Additon is : ",Ans)

    Ans = obj.Sub()
    print("Substraction  is : ",Ans)
if __name__ == "__main__":
    main()


