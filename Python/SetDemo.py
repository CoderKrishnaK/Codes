print("Demonstration of Sequence Data-type")


print("Demonstration of Set")

# Data : Heterogeneous
# Ordered : No
# Indexed : No
# Mutable : Yes
# Duplicates : No       Duplicate cant be store bcoz it is not stored it stores unique values


data = {11,21,51,101,21,11}
data1 = {11,90.80,True,"Hello"} #Heterogeneous

print("First set data:-",data)
print("Length of data",len(data))
print("Data is Heterogeneous:-",data1)
print("Data at uordered:",data1)
#print("Data at index 2 : ",data1[2])  error : set object is not subscritable
print("Data with unique elements:-",data)

print("Set is mutable")
data.add(211)
print("Data after insertion:",data)

data.remove(211)
print("Data after removal:-",data)

data.discard(201)
print("Data after discard:-",data)



