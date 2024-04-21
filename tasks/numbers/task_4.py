from typing import Callable
from algohub.algorithms.numbers.digits import get_digit

"""
Zad 6
Pobieraj od użytkownika dwie liczby do zmiennych o nazwach a i b typu
int tak długo, aż suma cyfr wszystkich liczb z przedziału <a, b> nie
będzie parzysta, a suma cyfr jedności liczb z tego przedziału nie
będzie większa od sumy cyfr dziesiątek tych liczb.
Draw two numbers into variables named a and b of type int, until the sum of the digits of all numbers
from the range <a, b> is not even, and the sum of the units digits of those numbers is not greater than
the sum of the tens digits of those numbers.

"""


def get_positive_int(message: str) -> int:
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
            else:
                print('Enter a positive integer')
        except ValueError:
            print('Please enter a valid integer')


def get_numbers_until_predicate(predicate_fn: Callable[[int, int], bool] = None) -> tuple[int, int]:
    while True:
        a, b = get_positive_int("Get first integer"), get_positive_int("Get second integer")

        if predicate_fn(a, b):
            return a, b


def is_condition_met(a: int, b: int, condition_fn: Callable[[int, int], bool]) -> bool:
    return condition_fn(a, b)


def is_digits_sum_even_and_units_greater_than_tens_sum(a: int, b: int) -> bool:
    if a >= b:
        raise ValueError("a must be lower than b")
    numbers = [n for n in range(a, b + 1)]
    print(numbers)
    digits_sum = sum([sum(int(d) for d in str(num)) for num in numbers])
    units_sum = sum([get_digit(num, 0) for num in numbers])
    tens_sum = sum([get_digit(d, 1) for d in numbers])

    if digits_sum % 2 != 0:
        return False
    if units_sum <= tens_sum:
        return False
    return True
