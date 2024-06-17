def prompt(user_message):
    print(f'==> {user_message}')


def get_user_input(prompt_message):
    prompt(prompt_message)
    return input()


def invalid_input(user_input, type_constructor, allow_zero=False):
    try:
        value = type_constructor(user_input)
        
        if not allow_zero and value == 0:
            print('Error: Zero is not allowed.')
            return True

        if value < 0:
            print('Error: Negative numbers are not allowed.')
            return True
    except ValueError:
        return True  # Return True if input is invalid or negative

    return False  # Return False if input is valid and non-negative


def calculate_monthly_payment(amount, apr, months):
    annual_interest_rate = float(apr) / 100
    monthly_interest_rate = annual_interest_rate / 12

    if monthly_interest_rate == 0:
        return float(amount) / int(months)
    else:
        return float(amount) * (
            monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-int(months)))
        )


def print_monthly_payment(payment):
    prompt(f'Your monthly payment is: ${payment:.2f}\n...')


def main():
    prompt('Welcome to Mortgage Calculator!\n...')
    loan_amount = get_user_input(
        'Please enter the total amount on your loan ' +
        '(example: 2050.38 = $2050.38): ')

    while invalid_input(loan_amount, float):
        print('Error: Invalid input. Please try again.\n...')
        loan_amount = get_user_input(
            'Please enter the total amount on your loan ' +
            '(example: 2050.38 = $2050.38): ')

    annual_percentage_rate = get_user_input(
        'Please enter the Annual Percentage Rate (APR) ' +
        '(example: 5 = 5%): ')

    while invalid_input(annual_percentage_rate, float, True):
        print('Error: Invalid input. Please try again.\n...')
        annual_percentage_rate = get_user_input(
            'Please enter the Annual Percentage Rate (APR) ' +
            '(example: 5 = 5%): ')

    loan_term_months = get_user_input(
        'Please enter the total length of the loan in months ' +
        '(example: 26 = 2 years and 2 months): ')

    while invalid_input(loan_term_months, int):
        print('Error: Invalid input. Please try again.\n...')
        loan_term_months = get_user_input(
            'Please enter the total length of the loan in months' +
            '(example: 26 = 2 years and 2 months): ')

    monthly_payment = calculate_monthly_payment(
        loan_amount, annual_percentage_rate, loan_term_months)

    print_monthly_payment(monthly_payment)

    run_again = get_user_input(
        'Would you like to run another calculation? Yes or no? ')

    if run_again and run_again.lower()[0] == 'y':
        main()


main()
