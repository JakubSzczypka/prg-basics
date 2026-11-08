def f(number, even):
    total = 0
    for digit_char in str(abs(number)):
        digit = int(digit_char)
        if even and digit % 2 == 0:
            total += digit
        elif not even and digit % 2 != 0:
            total += digit
    return total

if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))