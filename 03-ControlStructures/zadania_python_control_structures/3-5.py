month = int(input('Enter month number (1..12): '))
if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 28
print(f'Month {month} has {days} days')
