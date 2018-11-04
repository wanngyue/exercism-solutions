def validate_input(integer_number):
    if integer_number <= 0 or integer_number > 64:
        raise ValueError('Error')


def on_square(integer_number):
    validate_input(integer_number)
    return 2 ** (integer_number - 1)


def total_after(integer_number):
    validate_input(integer_number)
    return 1 if integer_number == 1 else total_after(integer_number - 1) + on_square(integer_number)
