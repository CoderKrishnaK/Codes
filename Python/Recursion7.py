# Accept Number
# Input :- 4
# Output :- 4 + 3 + 2 + 1

def Add(No):
    Sum = 0
    while(No > 0):
        Sum = Sum + No 
        No = No - 1
    return Sum           #BackTracking Head Recursion    
Ret = Add(4)
print("Result :",Ret)