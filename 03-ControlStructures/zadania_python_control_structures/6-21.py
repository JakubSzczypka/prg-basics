amount = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {amount // 5}")
amount %= 5
print(f"2 PLN coins: {amount // 2}")
amount %= 2
print(f"1 PLN coins: {amount}")
