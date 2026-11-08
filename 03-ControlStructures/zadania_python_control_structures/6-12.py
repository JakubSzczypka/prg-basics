amount_purchased = int(input("Number of products purchased: "))
price = float(input("Product price: "))
if amount_purchased > 2:
    total = (2 * price) + ((amount_purchased - 2) * price * 0.75)
else:
    total = amount_purchased * price
print(f"Amount to pay: {total:.2f}")
