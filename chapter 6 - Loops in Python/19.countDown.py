# print a countdown before something "exciting" happens
# like "Launching..." or "Happy New Year!".

import time

count = int(input("Enter the counter num :- "))
print("Countdown starts now:- ")

for num in range(count,0,-1):
    print(num)
    time.sleep(1)

print("Wohoo ! Haapy New Year")
