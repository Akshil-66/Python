class Student:
    schoolName = "ABC School"

    # Constructer
    # Add name 

    def __init__(self , name , course):
        self.name = name
        self.course = course
        print(self.name)
        print(self.course)


student1 = Student("Akshil" , "CE")  # init method will be called
print("Student 1 Name :- " , student1.name)
print("Student 1 Course :- " , student1.course)



student2 = Student("RadheKrishna" , "AI")  # init method will be called
print("Student 2 name :- " , student2.name)
print("Student 2 course :- " , student2.course)

