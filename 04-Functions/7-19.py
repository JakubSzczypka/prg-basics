def f(number):
    s = str(number)
    total = 0
    for i in range(10):
        c = s.count(str(i))
        if c > 1:
            total += i * c
    return total

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))