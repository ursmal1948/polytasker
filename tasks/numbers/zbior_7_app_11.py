from typing import Callable
import random

"""
Pobieraj od użytkownika liczbę całkowitą, dopóki nie będzie to liczba
palindromiczna, czyli taka która czytana od początku jest taka sama
jak czytana od końca. Oblicz sumę nieparzystych cyfr tej liczby.
"""


def draw_number_until(r_min: int,
                      r_max: int, condition_fn: Callable[[int], bool], finisher_fn: Callable[[int], int]):
    """
    Draws a number within a given range until a certain condition is met
    :param condition_fn: Callable[[int],int] a function that takes an integer and returns a boolean value
    :param finisher_fn: Callable[[int],int] a function to process the drawn number after the condition is met
    :param r_min: int the minimum value of the range (inclusive). Default is 100
    :param r_max: int the maximum value of the range (inclusive). Default is 999
    :return int: the processed number after the condition is met
    :raises ValueError: if range is incorrect (r_min greater than r_max)
    """
    if r_min > r_max:
        raise ValueError('Incorrect range')
    while not condition_fn(v := random.randint(r_min, r_max)):
        pass
    return finisher_fn(v)


def is_palindrome(n: int) -> bool:
    """
    Checks if a given integer is a palindrome
    :param n: int the integer to be checked
    :return bool: True if the integer is a palindrome, False otherwise
    """
    string_representation = str(n)
    return string_representation == string_representation[::-1]
