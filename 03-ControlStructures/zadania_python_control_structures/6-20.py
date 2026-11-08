dec = int(input("Enter decimal number: "))
original_dec = dec
binary = ""
if dec == 0:
    binary = "0"
while dec > 0:
    binary = str(dec % 2) + binary
    dec //= 2
print(f"{original_dec}(10) = {binary}(2)")
