"""Простой учебный калькулятор."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


if __name__ == "__main__":
    x = 12
    y = 4

    print("Учебный калькулятор")
    print("Сложение:", add(x, y))
    print("Вычитание:", subtract(x, y))
    print("Умножение:", multiply(x, y))
    print("Деление:", divide(x, y))
