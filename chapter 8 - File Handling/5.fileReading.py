# manually file closing 

file=open("report.txt" , "r")
data = file.read()
file.close()

# with keyword (Automatic file close)

with open("report.txt" , "r") as fule:
    data=fule.read()
    print("File data :- " , data)

# Read line by line

with open("newTextFile.txt" , "r") as file1:
    line1=file1.readline()
    line2=file1.readline()
    print("Line 1:-" , line1)
    print("Line 2:-" , line2)

    #Read all lines

    readLinesMethod=file1.readlines()
    print(readLinesMethod)