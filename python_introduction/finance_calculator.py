income = int(input("Enter your monthly income: "))
Monthly_Savings = int(input("Enter your total monthly expenses: "))
Projected_Savingss = income-Monthly_Savings
print(f"Your monthly savings are ${Projected_Savingss}.")

Projected_Savings = Projected_Savingss * 12 + (Projected_Savingss * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")