from django.core import exceptions


def only_letter_validator(current_str):
    for ch in current_str:
        if not ch.isalpha():
            raise exceptions.ValidationError('Name have to be with letters only!')


def telephone_number_length_validator(number):
    correct_length = 10
    correct_length_two = 13
    if len(number) < correct_length and len(number) < correct_length_two:
        raise exceptions.ValidationError(f'Telephone number length must be {correct_length} or {correct_length_two}')


def telephone_number_validator(number):
    correct_number = "08"
    correct_number_two = '+359'
    checking_symbols = number[:3]
    if checking_symbols != correct_number and correct_number_two != correct_number_two:
        raise exceptions.ValidationError(
            f'Telephone number must start with `{correct_number}` or `{correct_number_two}`!')
