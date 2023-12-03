def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not possible!!!"

# Usage
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 4))
print("Multiplication:", multiply(7, 2))
print("Division:", divide(8, 2))