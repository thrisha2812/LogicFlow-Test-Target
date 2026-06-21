def divide(a, b):
    return a / b

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)  # Bug: missing parentheses
    return total / count