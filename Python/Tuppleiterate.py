
Data = (11,21,51,101)

print("Output using for loop")
for no in Data:
    print(no,end = " ")
print()


print("Output using for loop with index")
for i in range(0,len(Data)):
    print(Data[i],end = " ")
print()

print("Output using while loop with index")
i = 0
while(i < len(Data)):
    print(Data[i], end = " ")
    i+=1


