def f(dice):
    if not dice:
        return 0
    max_val = int(dice[0])
    max_streak = 1
    current_streak = 1
    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > max_streak:
            max_streak = current_streak
            max_val = int(dice[i])
    return max_val

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))