# Prompting the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Asking the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projecting annual savings with interest
annual_savings = monthly_savings * 12  # Savings over one year
annual_savings_with_interest = annual_savings + (annual_savings * 0.05)  # Adding 5% interest

# Displaying the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings_with_interest:.2f}.")