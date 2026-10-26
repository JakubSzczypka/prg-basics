###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    result = sum(int(cyfra) for cyfra in str(abs(number)))

    return result

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')