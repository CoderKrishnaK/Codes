
values = [10,20,30,40]

print(values)

print(type(values))

print(len(values))  #len applicable for list only

values.insert(2,11) #(index,data)
print("Data after insert",values)

values.insert(15,89)
print("Size of list is now: ",len(values))
print("Data after insert 15 is: ",values)

print(values[0])    #by default \n newline is their
print(values[1])
print(values[2])
print(values[3])

values.append(50)
print(values)

values.remove(20)
print(values)

values.append(50)
print(values)

print(type(values[0]))
values.append(90.89)
print(values)


