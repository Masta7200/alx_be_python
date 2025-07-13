monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${savings:.2f}")
rate = 0.05  # 5% interest rate
time = 12  # 12 months
projected_savings = savings * 12 + (savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is ${projected_savings:.2f}")
