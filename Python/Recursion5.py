# Accept Number
# Input :- 4
# Output :- 4 3 2 1

def Display(No):
    if(No > 0):
        print(No)
        No = No - 1
        Display(No)     #Tail Recursion

Display(4)