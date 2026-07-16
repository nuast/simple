def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x / y

def div(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x // y

def mod(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x % y


def main():
    print("Testing calculator functions...")
    assert add(3, 4) == 7
    assert subtract(10, 5) == 5
    assert multiply(2, 3) == 6
    assert divide(10, 2) == 5
    assert divide(10, 0) == ValueError("Denominator cannot be zero.")
    assert divide(10, 3) == 3
    print("All tests passed!")


if __name__ == "__main__":
    main()