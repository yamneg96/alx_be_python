income = float(input("Enter your monthly income: "))

expenses = float(input("Enter your total monthly expenses: "))

savings = income - expenses

print("Your monthly savings are $"+str(int(savings))+".")

monthly_saving = savings * 12
projected_savings = monthly_saving + monthly_saving * 0.05

print("Projected savings after one year, with interest, is: $"+str(int(projected_savings))+".")
