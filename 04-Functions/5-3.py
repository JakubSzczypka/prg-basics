def input_string(message):
    return input(message)

def input_integer(message):
    return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message):
    val = input(message).lower()
    return val == 'y'

if __name__ == "__main__":
    first_name = input_string('Enter name: ')
    last_name = input_string('Enter last name: ')
    age = input_integer('Enter age: ')
    salary = input_real('Enter salary: ')
    is_salary_hidden = input_boolean('Hide salary? (y/n) ')

    print('DATA RECORD')
    print('===========')
    print('Name:', first_name, last_name)
    print('Age:', age)
    if not is_salary_hidden:
        print('Salary:', salary)