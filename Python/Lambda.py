# Normal Functions or Named Functions
def Add(No1,No2):
    return No1 + No2

# Lambda Functions / Unamed Functions
#lambda parameters : body

AddFunction = lambda A,B : A+B #Anonymous Function 


Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal Function: ",Ans1)
print("Addition using lambda Function: ",Ans2)

print("Type of lambda function is :-",type(AddFunction))