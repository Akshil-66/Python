# Create class student that takes 3 marks and has a method average().

class Student:

    def __init__(self , name , listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks
        
#   @saticmethod  write here to not write self in function perameter
    def average(self):
        sum=0
        for eachValue in self.listOfMarks:
            sum = sum+eachValue
        average=sum/3
        print("Average is :- " , average)


obj1 = Student("Akshil" , [90,98,99])
obj1.average()