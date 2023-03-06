# Accept Number
# Input :- 4
# Output :- 4 * 3 * 2 * 1

def Fact(No):
    if(No <= 0):
        return 1
    else:
        return (No * Add(No - 1))               

Ret = Fact(4)
print("Result :",Ret)

# Singleton class