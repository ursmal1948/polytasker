from typing import Callable
import random
from algohub.algorithms.numbers.primes import is_prime_basic

"""
Draw an integer until it becomes a palindrome, i.e., a number that remains the same when read
forwards and backwards. Calculate the sum of the odd digits of this number.
The function allows customization by accepting any condition and finishing function.
It draws a number that satisfies the specified condition and returns the result.
"""


def draw_and_process_number_with_condition(r_min: int = 100,
                                           r_max: int = 999,
                                           condition_fn: Callable[[int], bool] = lambda num: is_palindrome(num),
                                           finisher_fn: Callable[[int], int] = lambda num: num):
    """
    Draws a number within a given range until a certain condition is met.

    Parameters:
        r_min (int): The minimum value of the range (inclusive). Default is 100.
        r_max (int): The maximum value of the range (inclusive). Default is 999.
        condition_fn (Callable[[int], int]): A function that takes an integer and returns a boolean value.
        finisher_fn (Callable[[int], int]): A function to process the drawn number after the condition is met.

    Returns:
        int: The processed number after the condition is met.

    Raises:
        ValueError: If range is incorrect (r_min greater than r_max).

    Example:
        r_min = 100
        r_max = 999
    1.
        Input:
        Drawn number is 747
        condition_fn = lambda num: is_palindrome(num)
        finisher_fn =  lambda num: sum(int(d) for d in str(num) if int(d) % 2 == 1)
        Output: 14
    2.
        Input:
        Drawn number is 528
        condition_fn = lambda num: num >= 400
        finisher_fn = lambda num: max(int(d) for d in str(num))
        Output: 8
    """

    if r_min > r_max:
        raise ValueError('Incorrect range')
    while not condition_fn(v := random.randint(r_min, r_max)):
        pass
    return finisher_fn(v)


def is_palindrome(number: int) -> bool:
    """
    Checks if the given integer is a palindrome.

    Parameters:
        number (int): The integer to be checked.

    Returns:
        bool: True if the integer is a palindrome, False otherwise.
    """

    string_representation = str(number)
    return string_representation == string_representation[::-1]


# def main() -> None:
#     # result = draw_number_until(100, 999, lambda num: num > 300,
#     #                            lambda num: sum(int(d) for d in str(num) if int(d) % 2 == 1))
#     # print(f'RESULT: {result}')
#     print(draw_and_process_number_with_condition(condition_fn=lambda num: is_prime_basic(num)))
#
#
# if __name__ == '__main__':
#     main()
