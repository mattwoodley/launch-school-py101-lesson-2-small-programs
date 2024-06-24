"""
Rock, Paper, Scissors, Lizard, Spock Game

This script allows the user to play a game of rock, paper, scissors, lizard,
spock against the computer. The game prompts the user to choose one of the
five options and randomly selects a choice for the computer. The winner is
determined based on predefined rules. The game continues until the user or
the computer wins a specified number of rounds. The user can choose different
game modes (e.g., single round, best of 3, best of 5) and decide whether to
play another game after each round.

Functions:
- main(): Runs the game loop, handles game mode selection, and manages the
  overall flow of the game.
- play_one_round(scores): Plays one round of the game and updates the scores.
- update_score(scores, game_result): Updates the scores based on the game
  result.
- get_gamemode(): Prompts the user to choose a game mode.
- get_user_choice(): Prompts the user to choose rock, paper, scissors,
  lizard, or spock.
- get_computer_choice(): Randomly selects rock, paper, scissors, lizard, or
  spock for the computer.
- determine_winner(user_choice, computer_choice): Determines the winner of
  the game.
- display_score(scores): Displays the current scores.
- display_result(result, user_choice, computer_choice): Displays the result
  of the game.
- play_again(): Prompts the user to determine if they want to play another
  game.

Helper Functions:
- invalid_input(user_input, input_category): Checks if the user's input is
  valid.
- prompt(display_message): Prints a user message with a prefix.
- display_best_of(): Constructs a formatted string displaying the available
  game modes.
- display_choices(): Constructs a formatted string displaying available
  choices for the game.
- display_box(message): Displays a message within a box.
- clear_screen(): Clears the terminal screen.

Constants:
- MESSAGES: Dictionary containing various messages displayed to the user,
  loaded from a JSON file.
- VALID_CHOICES: List of valid choices for the game.
- CHOICES_SHORTHAND: Dictionary mapping shorthand user inputs to full choices.
- WINNING_CONDITIONS: Dictionary defining the winning conditions for each
  choice.
- GAMEMODES: Dictionary of available game modes.
- DISPLAY_TITLE: Formatted string displaying the title of the game.
- DISPLAY_GAMEMODES: Formatted string displaying available game modes.
- BEST_OF: Formatted string displaying the best of game modes for prompts.
- DISPLAY_CHOICES: Formatted string displaying choices for prompts.

The game starts by clearing the screen and displaying a welcome message.
"""

import os
import json
import random


# MAIN FUNCTIONS
def main():
    """
    Main function to run the rock, paper, scissors, lizard, spock game loop.

    Initializes the scores for the user and the computer. Continuously prompts
    the user to select a game mode and plays rounds until either the user or
    the computer wins the selected number of rounds. Displays the results after
    each round and updates the scores accordingly. At the end of each game, the
    user is asked if they want to play again. If the user chooses to continue,
    the screen is cleared and a new game starts. If not, a thank you message is
    displayed and the game exits.
    """
    scores = {
        'user': 0,
        'computer': 0
    }
    while True:
        selected_game_mode = get_game_mode()
        while (scores['user'] < selected_game_mode and
               scores['computer'] < selected_game_mode):
            play_one_round(scores)
            display_score(scores)

        if scores['user'] == selected_game_mode:
            display_box(MESSAGES['grand_winner'])
        elif scores['computer'] == selected_game_mode:
            display_box(MESSAGES['grand_loser'])

        # reset scores
        scores['user'] = 0
        scores['computer'] = 0

        if not play_again():
            break

        clear_screen()

    prompt(MESSAGES['thanks_for_playing'])


def play_one_round(scores):
    """
    Plays one round of the game and updates the scores.

    Args:
        scores (dict): Dictionary containing the current scores.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    prompt(MESSAGES['user_choice'].format(
        user_choice=user_choice.capitalize()))
    prompt(MESSAGES['computer_choice'].format(
        computer_choice=computer_choice.capitalize()))

    game_result = determine_winner(user_choice, computer_choice)
    update_score(scores, game_result)
    display_result(game_result, user_choice, computer_choice)


def update_score(scores, game_result):
    """
    Updates the scores based on the result of the game.

    Args:
        scores (dict): Dictionary containing the current scores.
        game_result (str): The result of the game ('win', 'loss', or 'draw').
    """
    if game_result == 'win':
        scores['user'] += 1
    elif game_result == 'loss':
        scores['computer'] += 1


def get_game_mode():
    """
    Prompts the user to choose a game mode.

    Returns:
        int: The selected game mode as an integer.
    """
    prompt(MESSAGES['display_game_modes'].format(game_modes=DISPLAY_GAME_MODES))
    prompt(MESSAGES['choose_game_mode'].format(best_of=BEST_OF))
    game_mode = input().strip().lower()

    while invalid_input(game_mode, 'game_mode'):
        prompt(MESSAGES['error_invalid'])
        prompt(MESSAGES['choose_game_mode'].format(best_of=BEST_OF))
        game_mode = input().strip().lower()

    return int(game_mode)


def get_user_choice():
    """
    Prompts the user to choose rock, paper, scissors, lizard, or spock.

    Returns:
        str: The user's valid choice.
    """
    prompt(MESSAGES['choose_rps'].format(choices=DISPLAY_CHOICES))
    choice = input().strip().lower()

    while invalid_input(choice, 'choice'):
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


def display_score(scores):
    """
    Displays the result of the game and calls the appropriate result handler.

    Args:
        result (str): The result of the game ('draw', 'win', or 'loss').
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
    """
    display_box(f'You: {scores['user']} | Computer: {scores['computer']}')


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
            message = MESSAGES['result_draw'].format(
                user_choice=user_choice.capitalize(),
                computer_choice=computer_choice.capitalize())
            display_box(message)
        case 'win':
            message = MESSAGES['user_wins'].format(
                user_choice=user_choice.capitalize(),
                computer_choice=computer_choice.capitalize())
            display_box(message)
        case 'loss':
            message = MESSAGES['user_loses'].format(
                user_choice=user_choice.capitalize(),
                computer_choice=computer_choice.capitalize())
            display_box(message)


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
def invalid_input(user_input, input_category):
    """
    Checks if the user's input is valid based on the category.

    Args:
        user_input (str): The user's input.
        input_category (str): The category of input ('choice' or 'game_mode').

    Returns:
        bool: True if the input is invalid, otherwise False.

    The function returns True in the following cases:
    - The user_input is not a string.
    - The input_category is 'choice' and user_input is not in VALID_CHOICES or
      CHOICES_SHORTHAND.
    - The input_category is 'game_mode' and
      user_input is not in GAMEMODES.values().
    
    Returns False if the input is valid.
    """
    if not isinstance(user_input, str):
        return True

    if input_category == 'choice':
        return (user_input not in VALID_CHOICES and
                user_input not in CHOICES_SHORTHAND)

    if input_category == 'game_mode':
        return user_input not in GAME_MODES.values()

    return False


def prompt(display_message):
    """
    Prints a user message with a prefix.

    Args:
        display_message (str): The message to be printed.
    """
    print(f'==> {display_message}')


def display_best_of():
    """
    Constructs a formatted string displaying the available game modes.

    Returns:
        str: Formatted string displaying the game modes, e.g. "1, 3, or 5".
    """
    game_mode_values = list(GAME_MODES.values())
    return f'{", ".join(game_mode_values[:-1])} or {game_mode_values[-1]}'


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


def display_box(message):
    """
    Displays a message within a box.

    Args:
        message (str): The message to be displayed.
    """
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

# Game modes available for the game
GAME_MODES = {
    'single': '1',
    'best_of_3': '3',
    'best_of_5': '5'
}

# Display the title of the game based on choices
DISPLAY_TITLE = ", ".join([choice.capitalize() for choice in VALID_CHOICES])

# Display the game modes available to play
DISPLAY_GAME_MODES = ", ".join(
    ['Best of ' + value for value in GAME_MODES.values()])

# Display the best of game modes for prompt messages
BEST_OF = display_best_of()

# Display choices for prompt messages
DISPLAY_CHOICES = display_choices()

# Start the game
clear_screen()
display_box((MESSAGES['welcome'].format(choices=DISPLAY_TITLE)))
main()
