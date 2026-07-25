#tuple basic

myTuple = (78,90,75)
studentTuple = ("Akshil" , "Harvi" , "Sumita" , "Akshil" , "Akshil") #we can put different type of values in one tuple like num,string etc...

print(studentTuple[0])

#empty tuple

intTuple = (1)
emptyTuple = ()
print(type(emptyTuple))
print(type(myTuple))
print(type(intTuple))

print(studentTuple.index("Akshil"))

print(studentTuple.count("Akshil"))

#tuples are immutable so we can not change value like this

studentTuple[1] = "Radha" #this get an error