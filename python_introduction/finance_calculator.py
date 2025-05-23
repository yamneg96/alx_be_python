income = input("Enter your monthly income: ")

expenses = input("Enter your total monthly expenses: ")

savings = float(income) - float(expenses)
savings = int(savings)

print("Your monthly savings are $"+str(savings)+".")

projected_savings = (savings * 12) + (savings * 12 * 0.05)
projected_savings = int(projected_savings)

print("Projected savings after one year, with interest, is: $"+str(projected_savings)+".")
