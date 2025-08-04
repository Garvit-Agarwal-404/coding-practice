print("Welcome to the tip Calculator!")
total_bill=float(input("What was the total bill? $ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people=int(input("How many people to split the bill?"))
per_person=round((total_bill*(1+(tip*0.01)))/no_of_people,2)
print(f"Each Person should pay: ${per_person}")




















