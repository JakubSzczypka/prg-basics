price = int(input("podaj cene: "))
discount = int(input("podaj znizke w %: "))

discountedpp = price*(discount/100)
print(f"podana cena: {price}")
print(f"podana znizka w %: {discount}")
print(f"podana cena ze znizka: {price-discountedpp}")
print(f"znizka w zl: {discountedpp}")