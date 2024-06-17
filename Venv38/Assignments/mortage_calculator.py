while True:

    def prompt(user_message):
        print(f'==> {user_message}')

    def get_user_input(prompt_message):
        prompt(prompt_message)
        return input()

    def validate_input(user_input, type_constructor):
        try:
            value = type_constructor(user_input)
            if value <= 0:
                print('Error: Negative numbers are not allowed.')
                return True
        except ValueError:
            return True  # Return True if input is invalid or negative

        return False  # Return False if input is valid and non-negative

    prompt('Mortgage Calculator!\n...')
    loan_amount = get_user_input('What is the loan amount? (Key: 2050.38 = $2050.38): ')

    while validate_input(loan_amount, float):
        print('Error: Invalid input. Please try again.\n...')
        loan_amount = get_user_input('What is the loan amount? (Key: 2050.38 = $2050.38): ')

    annual_percentage_rate = get_user_input('What is the Annual Percentage Rate? (Key: 5 = 5%): ')

    while validate_input(annual_percentage_rate, float):
        print('Error: Invalid input. Please try again.\n...')
        annual_percentage_rate = get_user_input('What is the Annual Percentage Rate? (Key: 5 = 5%): ')

    loan_term = get_user_input('How long is the loan? Answer in months (Key: 26 = 2 years and 2 months): ')

    while validate_input(loan_term, int):
        print('Error: Invalid input. Please try again.\n...')
        loan_term = get_user_input('How long is the loan? Answer in months (Key: 26 = 2 years and 2 months): ')

    annual_interest_rate = float(annual_percentage_rate) / 100
    monthly_interest_rate = annual_interest_rate / 12

    if monthly_interest_rate == 0:
        monthly_payment = float(loan_amount) / int(loan_term)
    else:
        monthly_payment = float(loan_amount) * (
        monthly_interest_rate /
        (1 - (1 + monthly_interest_rate) ** (-int(loan_term)))
    )

    prompt(f'Your monthly payment is: ${monthly_payment:.2f}\n...')
    run_again = get_user_input('Would you like to run another calculation? Yes or no? ')

    if not run_again or run_again.lower()[0] != 'y':
        break
