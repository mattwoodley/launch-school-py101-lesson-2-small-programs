"""
Rock, Paper, Scissors, Lizard, Spock Game

User will play against the Computer in a game of
rock, paper, scissors, lizard, spock.
This script will take input from the user, and then the computer will
select a response at random. The 2 values will then be compared, and depending
on the result, either user or computer will be declared the winner or in the
event of a draw the script will start again.
"""

import os
import json
import random


# MAIN FUNCTIONS
def main():
    """
    Main function that runs the rock, paper, scissors, lizard, spock game.
    Prompts the user for input, gets the computer's choice,
    determines the winner, displays the result,
    and prompts the user to continue or quit.
    """
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        prompt(MESSAGES['user_choice'].format(
            user_choice=user_choice.capitalize()))
        prompt(MESSAGES['computer_choice'].format(
            computer_choice=computer_choice.capitalize()))
        game_result = determine_winner(user_choice, computer_choice)
        display_result(game_result, user_choice, computer_choice)

        if not play_again():
            break

        clear_screen()

    prompt(MESSAGES['thanks_for_playing'])


def get_user_choice():
    """
    Prompts the user to choose rock, paper, scissors, lizard, or spock.

    Returns:
        str: The user's valid choice.
    """
    prompt(MESSAGES['choose_rps'].format(choices=DISPLAY_CHOICES))
    choice = input().strip().lower()

    while invalid_choice(choice):
        prompt(MESSAGES['error_invalid'])
        prompt(MESSAGES['choose_rps'].format(choices=DISPLAY_CHOICES))
        choice = input().strip().lower()

    if len(choice) <= 2:
        return CHOICES_SHORTHAND[choice]

    return choice


def get_computer_choice():
    """
    Randomly selects rock, paper, scissors, lizard, or spock for the computer.

    The choice is made from the VALID_CHOICES list.

    Returns:
        str: The computer's choice, which will be one of
        'rock', 'paper', 'scissors', 'lizard', or 'spock'.
    """
    return random.choice(VALID_CHOICES)


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the game.

    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.

    Returns:
        str: 'win' if the user wins,
             'loss' if the user loses,
             'draw' if it's a tie.
    """
    if user_choice == computer_choice:
        return 'draw'

    if computer_choice in WINNING_CONDITIONS[user_choice]:
        return 'win'

    return 'loss'


def display_result(result, user_choice, computer_choice):
    """
    Displays the result of the game and calls the appropriate result handler.

    Args:
        result (str): The result of the game ('draw', 'win', or 'loss').
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
    """
    match result:
        case 'draw':
            display_box('result_draw',
                        user_choice=user_choice.capitalize(),
                        computer_choice=computer_choice.capitalize())
        case 'win':
            display_box('user_wins',
                        user_choice=user_choice.capitalize(),
                        computer_choice=computer_choice.capitalize())
        case 'loss':
            display_box('user_loses',
                        user_choice=user_choice.capitalize(),
                        computer_choice=computer_choice.capitalize())


def play_again():
    """
    Prompts the user to determine if they want to play another game.

    Returns:
        bool: True if the user wants to continue, otherwise False.
    """
    prompt(MESSAGES['continue_playing'])
    continue_playing = input().strip().lower()
    return continue_playing in {'yes', 'y'}


# HELPER FUNCTIONS
def invalid_choice(choice):
    """
    Checks if the user's choice is valid
    (rock, paper, scissors, lizard, or spock).

    Args:
        choice (str): The user's choice.

    Returns:
        bool: True if the choice is invalid, otherwise False.
    """

    if not isinstance(choice, str):
        return True

    return choice not in VALID_CHOICES and choice not in CHOICES_SHORTHAND


def prompt(display_message):
    """
    Prints a user message with a prefix.

    Args:
        display_message (str): The message to be printed.
    """
    print(f'==> {display_message}')


def display_choices():
    """
    Constructs a formatted string displaying available choices for the game.

    Retrieves each key-value pair from CHOICES_SHORTHAND, formats as
    "{Value}/{Key}" with capitalized first letters, and joins into a
    comma-separated string.

    Returns:
        str: Formatted string displaying choices, e.g. "Rock/R, Paper/P,
             Scissors/Sc, Lizard/L, Spock/Sp".
    """
    choices_display = []
    for key, value in CHOICES_SHORTHAND.items():
        choices_display.append(f"{value.capitalize()}/{key.capitalize()}")
    choices_display = ", ".join(choices_display)
    return choices_display


def display_box(key, user_choice, computer_choice):
    """
    Displays a message from the MESSAGES dictionary within a box,
    with optional string formatting using keyword arguments.

    Args:
        key (str): The key to retrieve the message from the MESSAGES dictionary
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
    """
    message = MESSAGES[key].format(user_choice=user_choice,
                                   computer_choice=computer_choice)
    border = f"+{(len(message) + 2) * '-'}+"

    print(border)
    print(f'| {message} |')
    print(border)


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


# CONSTANTS

# Load messages from JSON file
with open('rock_paper_scissors_messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

# Valid choices for the game
VALID_CHOICES = [
    'rock',
    'paper',
    'scissors',
    'lizard',
    'spock'
]

# Shorthand mappings for user inputs
CHOICES_SHORTHAND = {
    'r':  'rock',
    'p':  'paper',
    'sc': 'scissors',
    'l':  'lizard',
    'sp': 'spock'
}

# Winning conditions for the game
WINNING_CONDITIONS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors']
}

# Display the title of the game based on choices
DISPLAY_TITLE = ", ".join([choice.capitalize() for choice in VALID_CHOICES])

# Display choices for prompt messages
DISPLAY_CHOICES = display_choices()

# Start the game
clear_screen()
prompt(MESSAGES['welcome'].format(choices=DISPLAY_TITLE))
main()
