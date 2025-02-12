total_price = 0
taxes = 0.2
while True:
    computer_part_price = input()
    if computer_part_price == "regular" or computer_part_price == "special":
        customer_type = computer_part_price
        break
    if float(computer_part_price) <= 0:
        print("Invalid price!")
        continue
    total_price += float(computer_part_price)

if total_price == 0:
    print("Invalid order!")
    exit()

total_taxes = taxes * total_price
final_price = total_price + total_taxes
if customer_type == "special":
    final_price -= 0.1 * final_price
print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price:.2f}$")
print(f"Taxes: {total_taxes:.2f}$")
print("-----------")
print(f"Total price: {final_price:.2f}$")
