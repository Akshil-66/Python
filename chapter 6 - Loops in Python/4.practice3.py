# write a program that prints the sum of first n natural numbers.
# for example , if n=5 , then output should be 1+2+3+4+5=15.

num = int(input("Enter how many number you want to add :- "))

sum=0

while num>=1:
    sum = num + sum
    num-=1

print(sum)