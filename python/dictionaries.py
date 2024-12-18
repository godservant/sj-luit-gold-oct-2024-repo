import random

var = {}

print(var)

print(type(var))

var2 = {"juice": "cranberry", "movie": "The Lion King", "fruit": "mango"}

print(var2)

print(var2["movie"])

var3 = {0: "number"} # you should not have integer indexes

print(var3)
print(var3[0])

var2["drank"] = "Patron"

print(var2)

var2["juice"] = "apple"

print(var2)

del var2["drank"]

print(var2)

print(dir(var2))

print(list(var2.keys()))

print(list(var2.values()))

print(var2.items())

print(list(var2.items()))

for k, v in var2.items():
    print(k, v)
    
dict_of_lists = {}
dict_of_lists["first"] =[0, 1, 2]
dict_of_lists["second"] =[0, 1, 2]
dict_of_lists["third"] =[0, 1, 2]

for k, v in dict_of_lists.items():
    print(k , v)
    
for k, v in dict_of_lists.items():
    print(k , v, type(v))
    for element in v:
        print(element)
        


    
    



      
      











