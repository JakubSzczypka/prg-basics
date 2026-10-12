###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Jakub'   # replace Anna with your name
surname = 'Szczypka' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
characters_in_fullname = len(name) + len(surname) + 1
print(f'Your full name has {characters_in_fullname}') # with a space between name and surname