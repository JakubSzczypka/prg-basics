plain_text = 'The early bird catches the worm'
encrypted_text = ''
for char in plain_text:
    if char == ' ':
        encrypted_text += ' '
    else:
        encrypted_text += chr(ord(char) + 1)
print(plain_text)
print(encrypted_text)
