print("__i am the new code__")

import csv

Date = input("Enter date: ")
Category = input("Enter the category: ")

while True:
    try:
        Amount = float(input("Enter the Amount: "))
        break
        
    except:
        print("please enter a valid number")
       

with open("expenses.csv","a", newline="") as f:
    write = csv.writer(f)
    write.writerow([Date,Category,Amount])

print("Saved!")

with open("expenses.csv", "r", newline="") as file:
    for row in file:
        print(row)