def m_to_cm(n):
    return n * 100

def cm_to_m(n):
    return n / 100

def cm_to_inches(n):
    return n / 2.54

def feet_inches_to_cm(feet, inches):
    return (feet * 12 + inches) * 2.54

if __name__ == "__main__":
    print(cm_to_inches(100))
    print(feet_inches_to_cm(5, 8))