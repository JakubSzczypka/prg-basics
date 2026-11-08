def f(detector):
    current_people = 0
    for action in detector:
        if action == '+':
            current_people += 1
            if current_people >= 3:
                return True
        elif action == '-':
            current_people -= 1
    return False

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))