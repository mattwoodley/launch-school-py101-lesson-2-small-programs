"""
1. Ask the user for the first number.
2. Ask the user for the second number.
3. Ask the user for an operation to perform.
4. Perform the operation on the two numbers.
5. Print the result to the terminal.
"""

print('Welcome to Calculator!')


def calculate(num1, num2, op):
    """
    Perform the specified arithmetic operation on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('+', '-', '*', '/').

    Returns:
    float or str: The result of the operation, or an error message if the
    operation is invalid or if there is a division by zero.
    """

    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Cannot divide by zero"
        case '*':
            return num1 * num2
        case _:
            return "Error: Invalid operation"


first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
operation = input(
    "Enter the operation you want to perform ('+', '-', '*', '/'): ")
result = calculate(first_number, second_number, operation)

print(f'{first_number} {operation} {second_number} = {result}')
