# Expense Tracker Project

expensesList = []  #List of expenses in form of dictionary

print(" Welcome to Expense Tracker ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choise :- "))

    if(choice==1):
        date = input("Enter the date :- ")
        category = input("Enter category (food,travel,etc...):- ")
        description = input("Add any details :- ")
        amount = float(input("Enter the amount :- "))

        expense = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n Expenses added successfully")

#2. VIEW ALL EXPENSES

    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expenses Added.")
        else:
            print("====Your Expense====")
            count=1
            for eachExpense in expensesList:
                print(f"{count} -> {eachExpense["date"]} , {eachExpense["category"]} , {eachExpense["description"]} , {eachExpense["amount"]} ")
                count+=1

#3. View Total Spending

    elif(choice==3):
        total=0
        for eachExpense in expensesList:
            total+=eachExpense["amount"]

        print("\n Total Expenses = " , total)

#4.exit

    elif(choice==4):
         print("Thanks for using our tool")
         break
    
    else:
        print("Invalid Choice : Try Again")