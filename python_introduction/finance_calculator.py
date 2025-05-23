income = float(input("Enter your monthly income: "))

expenses = float(input("Enter your total monthly expenses: "))

savings = income - expenses

print("Your monthly savings are $"+str(int(savings))+".")

projected_savings = (savings * 12) + (savings * 12 * 0.05)

print("Projected savings after one year, with interest, is: $"+str(int(projected_savings))+".")
