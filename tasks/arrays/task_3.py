import random
from typing import Callable
from collections import defaultdict
from dataclasses import dataclass, field
from tasks.common_functions import get_number

"""
Get from the user the size R of a one-dimensional array with elements of type int, and then draw elements into 
the array from the interval <0, 2*R> in such a way that no element in the array is repeated. Determine 
the maximum and minimum values among the elements in the array, as well as the element in the array with
the smallest sum of digits.
"""


def rand_number(r_min, r_max: int) -> int:
    """
    Generates a random length for the array within the specified range.

    Parameters:
        r_min (int): The minimum length of the array.
        r_max (int): The maximum length of the array.

    Returns:
        int: The randomly generated length of the array.

    Raises:
        ValueError: If r_min is greater than r_max.
    """

    if r_min > r_max:
        raise ValueError("Min value is greater than max value=")
    return random.randint(r_min, r_max)


@dataclass
class ArrayGenerator:
    """
    Generates an array of unique random numbers within a specified range.

    Attributes:
        size (int): The size of the array.
        r_min (int): The minimum value of the range (inclusive).
        r_max (int): The maximum value of the range (inclusive).
    """

    size: int
    r_min: int
    r_max: int

    def generate_unique_numbers(self) -> list[int]:
        """
         Generates a list of unique random numbers within the specified range.

         Returns:
             list[int]: A list of unique random numbers.
         """

        unique_numbers = set()
        while len(unique_numbers) < self.size:
            drawn_number = rand_number(self.r_min, self.r_max)
            unique_numbers.add(drawn_number)
        return list(unique_numbers)


@dataclass
class ArrayOperations:
    """
    Performs operations on an array of numbers.

    Attributes:
        numbers (list[int]): The list of numbers to perform operations on.
    """

    numbers: list[int] = field(default_factory=list)

    def get_extreme_element(self, extreme_fn: Callable[[list[int]], int]) -> int:
        """
        Finds the extreme element in the array based on the provided function.

        Parameters:
            extreme_fn (Callable[[list[int]], int]): The function to determine the extreme element.

        Returns:
            int: The extreme element in the array.

        Example:
            array_operations = ArrayOperations([1, 2, 3, 4, 5])
            Input: extrene_fn = lambda nums: min(nums)
            Output: 1
        """

        return extreme_fn(self.numbers)

    def process_elements_based_on_mapper(self,
                                         mapper_fn: Callable[[int], int] = lambda n: n,
                                         finisher_fn: Callable[[list[int]], int | list[int]] = max) \
            -> int | list[int]:
        """
         Groups elements based on a mapping function and performs operations on the groups.

         Parameters:
             mapper_fn (Callable[[int], int]): The function to map elements before grouping.
             finisher_fn (Callable[[list[int]], int | list[int]]): The function to finalize operations on the groups.

         Returns:
             int | list[int]: The result of the operation.

        Example:
            array_operations = ArrayOperations([123, 456, 789])
            Input: mapper_fn: lambda num: sum(int(d) for d in str(num)), finisher_fn: lambda nums: max(nums)
            Output: 789
         """

        grouped_elements = defaultdict(list)
        for n in self.numbers:
            key_ = mapper_fn(n)
            if key_:
                grouped_elements[key_].append(n)
        extreme_digit = finisher_fn(list(grouped_elements.keys()))
        result = grouped_elements[extreme_digit]
        return result[0] if len(result) == 1 else result


def main() -> None:
    array_size = get_number('Get array length')
    print(array_size)
    array_generator = ArrayGenerator(size=array_size, r_min=0, r_max=2 * array_size)
    unique_numbers = array_generator.generate_unique_numbers()
    print(f'Unique numbers: {unique_numbers}')
    array_operations = ArrayOperations(unique_numbers)
    smallest_number = array_operations.get_extreme_element(lambda nums: min(nums))
    print("-------------------(SMALLEST NUMBER)-------------------")
    print(smallest_number)
    highest_number = array_operations.get_extreme_element(lambda nums: max(nums))
    print("-------------------(HIGHEST NUMBER)-------------------")
    print(highest_number)
    print("-------------------(NUMBER/NUMBERS WITH SMALLEST DIGITS SUM)-------------------")
    number_with_smallest_digits_sum = array_operations.process_elements_based_on_mapper(
        lambda num: sum(int(d) for d in str(num)),
        lambda nums: min(nums)
    )
    print(number_with_smallest_digits_sum)
    print("-------------------(NUMBER/NUMBERS WITH HIGHEST DIGITS SUM)-------------------")

    number_with_highest_digits_sum = array_operations.process_elements_based_on_mapper(
        lambda num: sum(int(d) for d in str(num)),
        lambda nums: max(nums)
    )
    print(number_with_highest_digits_sum)


if __name__ == '__main__':
    main()
