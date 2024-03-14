from typing import Callable

"""
Zad 6
Pobieraj od użytkownika dwie liczby do zmiennych o nazwach a i b typu
int tak długo, aż suma cyfr wszystkich liczb z przedziału <a, b> nie
będzie parzysta, a suma cyfr jedności liczb z tego przedziału nie
będzie większa od sumy cyfr dziesiątek tych liczb.
"""


def get_int(message: str) -> int:
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
            else:
                print('Enter a positive integer')
        except ValueError:
            print('Please enter a valid integer')


def get_two_ints() -> tuple[int, int]:
    return get_int('Get first number'), get_int('Get second number')


def get_numbers_until_predicate(predicate_fn: Callable[[int, int], bool] = None) -> tuple[int, int]:
    while True:
        a, b = get_two_ints()

        if predicate_fn(a, b):
            return a, b


def get_digit(n: int, pos: int) -> int:
    if pos < 0:
        raise ValueError('The position is out of range')
    nn = abs(n) if n < 0 else n

    return (nn // 10 ** pos) % 10


def is_valid(a: int, b: int) -> bool:
    numbers = [n for n in range(a, b + 1)]
    digits_sum = sum([sum(int(d) for d in str(num)) for num in numbers])
    units_sum = sum([get_digit(d, 0) for d in numbers])
    tens_sum = sum([get_digit(d, 1) for d in numbers])

    if digits_sum % 2 != 0:
        return False
    if units_sum < tens_sum:
        return False
    return True
