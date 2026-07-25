# Read only the first line of bio.txt

import os  # rename file

with open("bio.txt" , "r") as f:
    line1 = f.readline()
    print(line1)

# print how many lines are present in bio.txt

with open("bio.txt" , "r") as f1:
    listOfLines = f1.readlines()
    print("Numver of lines in file :- " , len(listOfLines))

# rename file

# os.rename("bio.txt" , "Akshil.txt")

# os.remove("deleteFile.txt")

# try and except 

try:
    with open("notExit.txt" , "r") as f2:
        listOfLines1=f2.readlines()
        print("Output of readLines function" , listOfLines1)

except:
    print("That file does not exist")