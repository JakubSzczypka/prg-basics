current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))
decrease = ((previous_price - current_price) / previous_price) * 100
if decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(decrease)}%")
