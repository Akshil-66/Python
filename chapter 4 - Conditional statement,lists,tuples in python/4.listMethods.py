# methods in list

#indexing

#lists are mutable 

marks = [99,100,90,95]
print(marks[1:3])       #Slicing

print("Full list :- " , marks)

marks[0]= 98

print("After update:- " , marks)

#To find maximum or minimum value

print("Maximum value from marks is :- " , max(marks))
print("Maximum value from marks is :- " , min(marks))

#Add value at last position

marks.append(76)
print("After append list is :- " , marks)

#pop

marks.pop(1)
print("After pop vales are :- " , marks)

#remove

marks.remove(90)
print("Marks after remove 90 is :- " , marks)

#insert

marks.insert(1,200)
print("After inserting 200 marks are :- " , marks)

#sort 

marks.sort()
print("After sorting values are in order :- " , marks) #ascending order



#strings are immutable

name="Akshil"

name[0]="k" #this gets us error

print(name)