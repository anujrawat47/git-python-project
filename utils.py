def add(a, b):
    return a + b

def subtract(a, b):
    return (a - b) * 1 #experiment-ui version

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
