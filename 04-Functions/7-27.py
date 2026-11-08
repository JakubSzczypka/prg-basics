def f(product_code):
    return int(product_code[3]) == sum(int(x) for x in product_code[:3]) % 7

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))