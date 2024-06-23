"""
Rock, Paper, Scissors Game

User will play against the Computer in a game of rock, paper, scissors.
This script will take in input from the user, and then the computer will
select a response at random. The 2 values will then be compared, and depending
on the result, either user or computer will be declared the winner or in the
event of a draw the script will start again.
"""

import os
import json
import random

with open('rock_paper_scissors_messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_CONDITIONS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}


def prompt(display_message):
    """
    Prints a user message with a prefix.

    Args:
        display_message (str): The message to be printed.
    """
    print(f'==> {display_message}')


def invalid_choice(choice):
    """
    Checks if the user's choice is valid (rock, paper, or scissors).

    Args:
        choice (str): The user's choice.

    Returns:
        bool: True if the choice is invalid, otherwise False.
    """
    if choice.strip().lower() in VALID_CHOICES:
        return False

    return True


def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors.

    Returns:
        str: The user's valid choice.
    """
    choices_display = ', '.join(VALID_CHOICES)
    prompt(MESSAGES['choose_rps'].format(choices=choices_display))
    choice = input()

    while invalid_choice(choice):
        prompt(MESSAGES['error_invalid'])
        prompt(MESSAGES['choose_rps']).format(choices=choices_display)
        choice = input()

    return choice.lower()


def get_computer_choice():
    """
    Randomly selects rock, paper, or scissors for the computer.

    The choice is made from the VALID_CHOICES list.

    Returns:
        str: The computer's choice, which will be one of
        'rock', 'paper', or 'scissors'.
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
    """
    match result:
        case 'draw':
            display_box('result_draw', user_choice=user_choice,
                                       computer_choice=computer_choice)
        case 'win':
            display_box('user_wins', user_choice=user_choice,
                                       computer_choice=computer_choice)
        case 'loss':
            display_box('user_loses', user_choice=user_choice,
                                       computer_choice=computer_choice)


def display_box(key, user_choice, computer_choice):
    """
    Displays a message from the MESSAGES dictionary within a box,
    with optional string formatting using keyword arguments.

    Args:
        key (str): The key to retrieve the message from the MESSAGES dictionary
        **kwargs: Additional keyword arguments for string formatting.
    """
    message = MESSAGES[key].format(user_choice=user_choice,
                                   computer_choice=computer_choice)
    border = f"+{(len(message) + 2) * '-'}+"

    print(border)
    print(f'| {message} |')
    print(border)

def play_again():
    """
    Prompts the user to determine if they want to play another game.

    Returns:
        bool: True if the user wants to continue, otherwise False.
    """
    prompt(MESSAGES['continue_playing'])
    continue_playing = input().lower()
    return continue_playing == 'yes' or continue_playing == 'y'


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
    Main function that runs the rock, paper, scissors game.
    Prompts the user for input, gets the computer's choice,
    determines the winner, displays the result,
    and prompts the user to continue or quit.
    """
    clear_screen()
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        prompt(MESSAGES['user_choice'].format(user_choice=user_choice))
        prompt(MESSAGES['computer_choice'].format(
            computer_choice=computer_choice))
        game_result = determine_winner(user_choice, computer_choice)
        display_result(game_result, user_choice, computer_choice)

        if not play_again():
            break

        clear_screen()

    prompt(MESSAGES['thanks_for_playing'])


prompt(MESSAGES['welcome'])
main()

# Change win draw and losses to display within a box to separate from prompts
