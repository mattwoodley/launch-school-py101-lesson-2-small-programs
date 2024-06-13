import json

with open('calculator_messages.json', encoding='utf-8') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

def messages(key, lang='en'):
    return MESSAGES[lang][key]

def prompt(key):
    print(f'==> {key}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

while True:

    prompt(messages('welcome', LANGUAGE))

    prompt(messages('number_1', LANGUAGE))
    number_1 = input()

    while invalid_number(number_1):
        prompt(messages('invalid_number', LANGUAGE))
        number_1 = input()

    prompt(messages('number_2', LANGUAGE))
    number_2 = input()

    while invalid_number(number_2):
        prompt(messages('invalid_number', LANGUAGE))
        number_2 = input()

    prompt(messages('operation', LANGUAGE))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(messages('invalid_operation', LANGUAGE))
        operation = input()

    match operation:
        case '1':
            output = float(number_1) + float(number_2)
        case '2':
            output = float(number_1) - float(number_2)
        case '3':
            output = float(number_1) * float(number_2)
        case '4':
            if float(number_2) == 0:
                output = messages('error_divide_by_zero', LANGUAGE)
            else:
                output = float(number_1) / float(number_2)

    if isinstance(output, str):
        prompt(output)
    else:
        prompt(f"{messages('result', LANGUAGE)} {output}")
    print()

    prompt(messages('run_again?', LANGUAGE))
    answer = input()

    if answer and answer[0].lower() != messages('answer', LANGUAGE):
        break

    print()
