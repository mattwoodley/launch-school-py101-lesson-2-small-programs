"""
Mortgage Calculator

This script allows users to calculate monthly mortgage payments based on
user-provided loan amount, annual percentage rate (APR),
and loan term in months.
"""

import math
import os

def prompt(display_message):
    """
    Prints a user message with a prefix.

    Args:
        display_message (str): The message to be printed.
    """
    print(f'==> {display_message}')


def get_user_input(prompt_message):
    """
    Prompts the user for input and returns the entered value.

    Args:
        input_prompt (str): The message prompting the user for input.

    Returns:
        str: The user's input.
    """
    prompt(prompt_message)
    return input()


def invalid_input(user_input, type_constructor, allow_zero=False):
    """
    Validates user input, checking if it can be converted to a specified type
    and meets certain conditions.

    Args:
        user_input (str): The input provided by the user.
        type_constructor (type): The type to which the input
        should be converted.
        allow_zero (bool, optional): Whether zero is permitted
        as valid input. Defaults to False.

    Returns:
        bool: True if the input is invalid, otherwise False.
    """
    try:
        value = type_constructor(user_input)
    except ValueError:
        return True

    if not allow_zero and value == 0:
        print('Error: Zero is not allowed.')
        return True

    if math.isinf(value):
        print('Error: Infinite is not allowed.')
        return True

    if math.isnan(value):
        print('Error: NaN is not allowed.')
        return True

    if value < 0:
        print('Error: Negative numbers are not allowed.')
        return True

    return False


def calculate_monthly_payment(loan_amount,
                              annual_interest_rate_percentage,
                              loan_term_months):
    """
    Calculates the monthly payment for a loan given the loan amount,
    annual interest rate (as a percentage), and loan term in months.

    Args:
        loan_amount (float): The total amount of the loan.
        annual_interest_rate_percentage (float): The annual 
        interest rate as a percentage (e.g., 5 for 5%).
        loan_term_months (int): The length of the loan term in months.

    Returns:
        float: The monthly payment amount.
    """
    annual_interest_rate = float(annual_interest_rate_percentage) / 100
    monthly_interest_rate = annual_interest_rate / 12

    if monthly_interest_rate == 0:
        return float(loan_amount) / int(loan_term_months)

    return float(loan_amount) * (
        monthly_interest_rate /
        (1 - (1 + monthly_interest_rate) ** (-int(loan_term_months)))
    )


def print_monthly_payment(payment_amount):
    """
    Prints the monthly payment amount.

    Args:
        payment_amount (float): The amount of the monthly payment.
    """
    prompt(f'Your monthly payment is: ${payment_amount:.2f}\n...')


def get_loan_amount():
    """
    Prompts the user to input the total loan amount
    and validates the input.

    The function repeatedly prompts the user until a valid,
    positive float is entered.

    Returns:
        float: The valid loan amount entered by the user.
    """
    loan_amount = get_user_input(
        'Please enter the total amount on your loan ' +
        '(example: 2050.38 = $2050.38): ')

    while invalid_input(loan_amount, float):
        print('Error: Invalid input. Please try again.\n...')
        loan_amount = get_user_input(
            'Please enter the total amount on your loan ' +
            '(example: 2050.38 = $2050.38): ')

    return loan_amount


def get_apr():
    """
    Prompts the user to input the Annual Percentage Rate (APR)
    and validates the input.

    The function repeatedly prompts the user until a valid,
    non-negative float is entered.

    Returns:
        float: The valid annual percentage rate entered by the user.
    """
    annual_percentage_rate = get_user_input(
        'Please enter the Annual Percentage Rate (APR) ' +
        '(example: 5 = 5%): ')

    while invalid_input(annual_percentage_rate, float, True):
        print('Error: Invalid input. Please try again.\n...')
        annual_percentage_rate = get_user_input(
            'Please enter the Annual Percentage Rate (APR) ' +
            '(example: 5 = 5%): ')

    return annual_percentage_rate


def get_loan_months():
    """
    Prompts the user to input the total loan term in months
    and validates the input.

    The function repeatedly prompts the user until a valid,
    positive integer is entered.

    Returns:
        int: The valid loan term in months entered by the user.
    """
    loan_term_months = get_user_input(
        'Please enter the total length of the loan in months ' +
        '(example: 26 = 2 years and 2 months): ')

    while invalid_input(loan_term_months, int):
        print('Error: Invalid input. Please try again.\n...')
        loan_term_months = get_user_input(
            'Please enter the total length of the loan in months' +
            '(example: 26 = 2 years and 2 months): ')

    return loan_term_months


def continue_calculating():
    """
    Prompts the user to determine if they want to run another calculation.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    response = get_user_input(
        'Would you like to run another calculation? Yes or no? ')
    return response.lower() == 'yes'


def clear_screen():
    """
    Clears the terminal screen.

    Checks the operating system and executes the appropriate command:
    - For Unix-like systems (Linux, macOS), it uses the 'clear' command.
    - For Windows systems, it uses the 'cls' command.
    """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def main():
    """
    Main function that runs the mortgage calculator.

    - Prompts the user for input
    - Validates each input
    - Calculates the monthly payment
    - Prints the payment
    - Prompts the user to decide if they want to perform another calculation
    - If the user chooses to continue: clears the screen and reruns the script
    - Else the program ends
    """

    loan_amount = get_loan_amount()
    annual_percentage_rate = get_apr()
    loan_term_months = get_loan_months()

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                annual_percentage_rate,
                                                loan_term_months)

    print_monthly_payment(monthly_payment)

    if continue_calculating():
        clear_screen()
        main()


prompt('Welcome to Mortgage Calculator!')
main()
