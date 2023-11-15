"""
## Tip Calculator
Calculates the total to be paid including tip
"""
print("Welcome to the tip calculator")
bill = float(input("What is the total bill : $"))
tip = float(input("What is the tip percent : "))
people = int(input("How many people to split the bill : "))
final_bill = round(bill*(1+tip/100)/people,2)
print(f"Each person would pay ${'{:.2f}'.format(final_bill)}")