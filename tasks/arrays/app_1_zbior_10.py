import random
from typing import Callable
from tasks.common_functions import get_array_length
from algohub.algorithms.numbers.primes import is_prime_basic

"""
Prepare a one-dimensional array of integers. The dimension of the array
is randomly chosen from the interval [10, 100]. Each element of the array
has a value randomly chosen from the interval [100, 200] until the sum
of its digits is a number having exactly two divisors, excluding 1 and 
the number itself. Determine the sum of the four largest elements in 
the array. Note that when the array contains elements like:
1 1 1 2 2 2 3 3 4 4 5 5, the four largest elements are considered 
as 5, 4, 3, and 2.
"""


def generate_n_numbers_until_predicate(size: int, r_min: int = 100, r_max: int = 200,

                                       predicate_fn: Callable[[int], bool] = lambda n: n % 2 == 1):
    """
    Generate a list of numbers until the specified predicate function is satisfied.

    Parameters:
        size (int): The size of the list to be generated.
        r_min (int): The minimum value for number generation (default is 100).
        r_max (int): The maximum value for number generation (default is 200).
        predicate_fn (Callable[[int], bool]): The predicate function to satisfy (default is odd numbers).

    Returns:
        list[int]: A list of numbers satisfying the predicate function.

    Raises:
        ValueError: If the range (r_min, r_max) is not correct.

    Example:
        Input: size = 5, r_min = 100, r_max = 200, predicate_fn = lambda n: is_prime_basic(calculate_digits_sum(n))
        Output: [199, 133, 137, 188, 111]
    """

    if r_min > r_max:
        raise ValueError('Range is not correct')
    numbers = []
    while size > len(numbers):
        drawn_number = random.randint(r_min, r_max)
        if predicate_fn(drawn_number):
            numbers.append(drawn_number)
    return numbers


def process_n_extreme_elements(
        numbers: list[int], count: int, extreme_fn: Callable[[list[int], int], list[int]],
        finisher_fn: Callable[[list[int]], int]
) -> int:
    """
    Calculate the sum of the n extreme elements in a list.

    Parameters:
        numbers (list[int]): The list of numbers.
        count (int): The number of extreme elements to consider.
        extreme_fn (Callable[[list[int], int], list[int]]): A function to determine the extreme elements.
        finisher_fn (Callable[[list[int]], int]): A function to calculate the sum of the extreme elements.

    Returns:
        int: The sum of the extreme elements.

    Raises:
        ValueError: If there are not enough values in the list.

    Example:
        Input: numbers = [10,20,30,40,50,60], count = 3, extreme_fn = lambda nums, count: get_highest(nums, count)
               finisher_fn = lambda nums: sum(nums)
        Output: 150
    """

    if count > len(numbers):
        raise ValueError('Not enough values')
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers)
    extreme_numbers = extreme_fn(sorted_numbers, count)
    return finisher_fn(extreme_numbers)


def calculate_digits_sum(n: int) -> int:
    """
    Calculate the sum of digits of a number.

    Parameters:
        n (int): The number to calculate the sum of its digits.

    Returns:
        int: The sum of the digits of the number.

    Example:
        Input: 25024
        Output: 13
    """

    nn = abs(n) if n < 0 else n
    return sum(int(d) for d in str(nn))


def get_highest(numbers: list[int], count: int) -> list[int]:
    """
    Get the highest n elements from a list.

    Parameters:
        numbers (list[int]): The list of numbers.
        count (int): The number of highest elements to retrieve.

    Returns:
        list[int]: The highest n elements from the list.

    Example:
        Input: numbers = [1, 2, 3, 4, 5, 6], count = 4
        Output: [3,4,5,6]
    """

    return numbers[-count:]


def main() -> None:
    array_length = get_array_length(10, 100)
    print(f'Array length: {array_length}')
    numbers = generate_n_numbers_until_predicate(size=array_length,
                                                 predicate_fn=lambda n: is_prime_basic(calculate_digits_sum(n)))
    print(f'Numbers: {numbers}')
    sum_of_extreme_elements = process_n_extreme_elements(numbers, 4,
                                                         lambda nums, count: get_highest(nums, count),
                                                         lambda nums: sum(nums))
    print(f'Sum of extreme elements: {sum_of_extreme_elements}')


if __name__ == '__main__':
    main()
