# Dictionary Basics

student = {
    "name"  : "Akshil",
    "city" : "Rajkot",
    "age" : 18 ,
    "rollNumber" : 1005 ,
    "name" : "RadheKrishna"

    #these keys (name,city,age,rollNumber) are unique keys and if we 
    # write same key name so its override privious one
}

print("Student details type :- " , type(student))
print("Name from student dictionary :-" , student["name"])
print("Print full dictionary :- " , student)
print("Print city :- " , student["city"])

#Update anything in dictionary

student["city"] = "London"
print("Print updated city :- " , student["city"])

# Add new key in dictionary

student["FavSub"] = "Maths"
print("Print new key :- " , student["FavSub"])
print("Print full dictionary :- " , student )

# Remove key in dictinary

student.pop("FavSub")
print("After remove FavSub :- " , student)

print(student.keys())
print(student.values())
print(student.items()) #shows in tuples