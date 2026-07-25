class Student:
    schoolName = "ABC School"

    # Constructer

    def __init__(self):
        print("Whenever a new object created i am called automatically ")
        print(self)


student1 = Student()  # init method will be called
print("Student 1 :- " , student1)

student2 = Student()  # init method will be called