def count_letter(text, letter):
    return text.count(letter)

if __name__ == "__main__":
    text = "You never get a second chance to make a first impression"
    print(f"The number of letter 'e': {count_letter(text, 'e')}")