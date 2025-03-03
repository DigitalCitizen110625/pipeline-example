def add(a, b):
    # Intentional bug: using subtraction instead of addition.
    return a - b

if __name__ == '__main__':
    result = add(2, 3)
    print("2 + 3 =", result)
