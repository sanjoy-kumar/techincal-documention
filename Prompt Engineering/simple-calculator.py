"""
Act as a Python expert. 
Task: Write a script to do simple calculation as a calculator. 
Constraints: 
    - Clean code 
    - Exception handling 
Output format: 
    - Complete script 
    - Example usage
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def calculate(num1: float, num2: float, operator: str) -> float:
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operator not in operations:
        raise ValueError("Invalid operator. Use +, -, *, or /")

    return operations[operator](num1, num2)


def main() -> None:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        result = calculate(num1, num2, operator)
        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Input Error: {ve}")

    except ZeroDivisionError as zde:
        print(f"Math Error: {zde}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
