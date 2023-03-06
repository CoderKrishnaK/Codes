Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}

print("Data of Dictionary:-",Batches)

print("Data traversal using for loop")

for x in Batches:   #for each loop 
    print(x)


print("Data traversal using for loop")
for x in Batches:   #for each loop
    print(x,":",Batches[x])


print("Data traversal using for loop")
for x in Batches:   #for each loop
    print(x,Batches.get(x))

keysBatches = Batches.keys()
print(keysBatches)
print(type(keysBatches))    #class dict_keys is a list

valuesBatches = Batches.values()
print(valuesBatches)
print(type(valuesBatches))

