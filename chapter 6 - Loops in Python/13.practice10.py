# write a program that prints the multiplication table of any number
# entered by the user using a for loop.

num = int(input("Enter any number :- "))

for numb in range(1,11):
    print(f"{num} * {numb} = {num*numb}")
    