def month(n):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    return months[n - 1]

if __name__ == "__main__":
    n = int(input("Enter month number: "))
    print(f"The name of month {n} is {month(n)}")