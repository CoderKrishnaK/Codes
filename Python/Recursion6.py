# Accept Number
# Input :- 4
# Output :- 4 3 2 1

def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)
        print(No)           #BackTracking Head Recursion    
Display(4)