tax_per_year = int(input("Enter the annual tax: "))
sneakers_price = 0.6 * tax_per_year
equipment_price = 0.8 * sneakers_price
ball_price = 1/4 * equipment_price
accessories_price = 1/5 * ball_price

total_expenses = tax_per_year + sneakers_price + equipment_price + ball_price + accessories_price
print(f"Total expenses: {total_expenses:.2f}")
