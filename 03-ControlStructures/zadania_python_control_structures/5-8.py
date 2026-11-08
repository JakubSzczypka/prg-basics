balance = 0
pin = "1111"
while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        print(f"Balance: {balance}")
    elif choice == '2':
        amount = float(input("Amount to deposit: "))
        balance += amount
    elif choice == '3':
        amount = float(input("Amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds")
    elif choice == '4':
        entered_pin = input("Enter PIN: ")
        if entered_pin == pin:
            print("PIN is correct")
        else:
            print("Incorrect PIN")
    elif choice == '5':
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN changed")
        else:
            print("Invalid PIN format")
    elif choice == '6':
        break
