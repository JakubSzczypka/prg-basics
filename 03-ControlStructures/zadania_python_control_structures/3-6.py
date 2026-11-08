month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False
if month in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= day <= 31:
        day_ok = True
elif month in [4, 6, 9, 11]:
    if 1 <= day <= 30:
        day_ok = True
elif month == 2:
    if 1 <= day <= 28:
        day_ok = True
message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')
