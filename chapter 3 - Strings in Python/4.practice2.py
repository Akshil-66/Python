# Question on slicing
# take input and print middle 3 charcter , last 2 character

str = input("Enter the value :- ")

mid = len(str)//2          # we use // for remove decimal part
output1 = str[mid-1:mid+2]
output2 = str[-2:]


print("Middle 3 characters are :-" , output1)
print("Last 2 characters are :-" , output2) 