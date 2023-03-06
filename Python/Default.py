def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIValue = 3.14

    #positional argument
    Ans = Area(RValue,PIValue)              #Ans = Area(10.5,3.14)
    print("Area of circle is :-",Ans)

    #keyword argument
    Ans = Area(PI = PIValue, Radius = RValue) #keyword to positional argument
    print("Area of circle is :-",Ans)

    #Positional argument and second is default argument
    Ans = Area(10.5)
    print("Area of circle is :-",Ans)

    #keyword argument and second is default
    Ans = Area(Radius = 10.5)
    print("Area of circle is :-",Ans)

    #keyword Arguments
    Ans = Area(PI = 7.10 ,Radius = 10.5)
    print("Area of circle is :-",Ans)
if __name__ == "__main__":
    main()