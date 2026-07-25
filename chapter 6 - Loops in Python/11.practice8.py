# write a program to print numbers from 1 to 50 but print "RadheKrishna"
#instead of numbers that are multiple of 5.

for num in range(1,50):
    if(num%5==0):
        print("RadheKrishna")
    else:
        print(num)
    num+=1