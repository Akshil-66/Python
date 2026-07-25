# you are given a list of programming languages :
# ["Python" , "Java" , "C++" , "Python" , "Java" , "C"]
# convert it into a set and print how many unique languages Divya knows.

programmingList = ["Python" , "Java" , "C++" , "Python" , "Java" , "C"]
print(type(programmingList))

# how to convert list into set

programmingSet = set(programmingList)
print(type(programmingSet))

print("Divya knows these many langauges :- " , len(programmingSet))