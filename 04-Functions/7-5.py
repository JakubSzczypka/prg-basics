def in_range(number, x, y):
    return x <= number <= y

if __name__ == "__main__":
    n = 7
    print(f"A number: {n}")
    print(f"Number {n} in the range <2,15>: {'yes' if in_range(n, 2, 15) else 'no'}")