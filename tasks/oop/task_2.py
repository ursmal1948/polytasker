"""
2. In the text file prepared by you, place three integers separated by semicolons in each line.The format of a sample
line is: 32;56;10. The number of lines is arbitrary. Prepare a class named Lists, which contains three lists
of integers. The constructor of the class fetches data from a text file named as an argument to the constructor.
The first list stores the smallest numbers from each line, the second list stores the second largest numbers
from each line, and the third list stores the largest numbers from each line. We agree that we call a file with
your data perfect if the first list has all elements smaller than the second list, and the second list has all
elements smaller than the third list. Write methods in the Lists class to solve the following problems:

->> Check if the file prepared by you is a perfect file? Which numbers from the first list and which numbers
from the second list should be removed to meet the condition for a perfect file? Present a list of these numbers.

Input: filename:'data/numbers'
numbers:28;56;13
        78;25;17
        99;19;58
        98;60;29
        432;10;49

Output: (False, {0: [29], 1: [58, 60]})
False -> file is not perfect
Numbers to delete from smallest_numbers: 29 and from middle_numbers: 58 & 60

Example numbers to use for tasks below
smallest: [13, 17, 19, 29, 10]
middle:   [28, 25, 58, 60, 49]
highest:  [56, 78, 99, 98, 432]

->> Determine the difference between the largest element of the first list and the smallest element of the
second list. How many elements in the third list are divisible by this calculated difference, if it is not zero?

largest element of the first list: 29
smallest element of the second list: 25

Output:
difference = 4
elements in the third list divisible by difference: 56 & 432


->> Determine which of the three lists in the Lists class has the longest non-decreasing sequence among its
elements. Return the index corresponding to the list (1 being the smallest, 3 being the highest)

Output: 1 (because list with the smallest numbers has the longest non-decreasing sequence)


->> Sort the three lists in descending order and check for which index the difference between elements of the
three lists is the smallest, and for which index the difference between elements of the three lists is the largest.

Sorted numbers
[29, 19, 17, 13, 10]
[60, 58, 49, 28, 25]
[432, 99, 98, 78, 56]

Output: 0 (largest difference between elements in the lists is equal 806)
"""
import re
from dataclasses import dataclass, field
from typing import Callable
from collections import defaultdict
from typing import Self


@dataclass
class FileReader:
    @staticmethod
    def read(filename: str) -> list[str]:
        """
        Read lines from a text file.

        Parameters:
            filename (str): The name of the file to read.

        Returns:
            list[str]: A list containing lines read from the file.
        """

        with open(filename, 'r') as f:
            return f.read().splitlines()


@dataclass
class Row:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    @classmethod
    def parse(cls, line: str, regex: str = r'(\d+;){2}\d+') -> Self:
        if not re.match(regex, line):
            raise ValueError(f"Line does not match regex: {line}")
        numbers = [int(n) for n in line.split(";")]
        return cls(numbers)

    def get_numbers(self) -> list[int]:
        return self.numbers


@dataclass
class Numbers:
    smallest_numbers: list[int] = field(default_factory=list)
    middle_numbers: list[int] = field(default_factory=list)
    highest_numbers: list[int] = field(default_factory=list)

    def get_all_numbers(self) -> list[list[int]]:
        return [self.smallest_numbers, self.middle_numbers, self.highest_numbers]

    @classmethod
    def from_file(cls, filename: str) -> Self:
        """
         Create Numbers object from data in a text file.

         Parameters:
             filename (str): The name of the file containing data.

         Returns:
             Numbers: An instance of Lists populated with data from the file.
         """

        lines = FileReader.read(filename)
        numbers = [Row.parse(line).get_numbers() for line in lines]
        smallest_numbers = [min(sub_numbers) for sub_numbers in numbers]
        middle_numbers = [sorted(sub_numbers)[1] for sub_numbers in numbers]
        highest_numbers = [max(sub_numbers) for sub_numbers in numbers]
        return cls(smallest_numbers, middle_numbers, highest_numbers)

    @staticmethod
    def _calculate_values_to_delete(numbers: list[int], min_value: int) -> list[int]:
        return [n for n in numbers if n > min_value]

    def _get_values_to_delete(self):
        min_number_from_middle_numbers = min(self.middle_numbers)
        min_number_from_highest_numbers = min(self.highest_numbers)

        numbers_to_delete = {
            0: self._calculate_values_to_delete(self.smallest_numbers, min_number_from_middle_numbers),
            1: self._calculate_values_to_delete(self.middle_numbers, min_number_from_highest_numbers)
        }
        return numbers_to_delete

    def is_file_perfect(self) -> bool | tuple[bool, dict[int, list[int]]]:
        """
        Check if the file meets the 'perfect file' conditions.

        Returns:
            bool | tuple[bool, dict[int, list[int]]]:
                If the file is perfect, returns True.
                If not perfect, returns a tuple containing False  and a dictionary with numbers
                 to delete from each list.
        """

        numbers_to_delete = self._get_values_to_delete()
        values = [n for n in numbers_to_delete.values() if n]
        return True if not values else (False, numbers_to_delete)

    def get_diff_between(self,
                         finisher_fn_1: Callable[[list[int]], int],
                         finisher_fn_2: Callable[[list[int]], int]) \
            -> int:
        """
        Calculate the difference between two finisher functions applied to different lists.

        Parameters:
            finisher_fn_1 (Callable[[list[int]], int]): A function to process the first list.
            finisher_fn_2 (Callable[[list[int]], int]): A function to process the second list.

        Returns:
            int: The difference between the results of finisher_fn_1 and finisher_fn_2.
        """

        return abs(finisher_fn_1(self.smallest_numbers) - finisher_fn_2(self.middle_numbers))

    def count_elements_meeting_condition(self, condition_fn: Callable[[int], bool]) -> int:
        """
         Count elements in the third list meeting a specified condition.

         Parameters:
             condition_fn (Callable[[int], bool]): A function defining the condition.

         Returns:
             int: The count of elements meeting the condition in the third list.
         """
        return sum(1 for num in self.highest_numbers if condition_fn(num))

    @staticmethod
    def get_length_of_non_decreasing_sequence(numbers: list[int]) -> int:
        """
        Calculate the length of the longest non-decreasing sequence in a list.

        Parameters:
            numbers (list[int]): The list of numbers.

        Returns:
            int: The length of the longest non-decreasing sequence.
        """

        if numbers[1] < numbers[0]:
            return 0
        count = 1
        for i in range(2, len(numbers)):
            if numbers[i] >= numbers[i - 1]:
                count += 1
            else:
                return count
        return count

    def find_extreme_non_decreasing_sequence(self, extreme_fn: Callable[[list[int]], int]) -> int | list[int]:
        """
        Finds the list with the longest non-decreasing sequence.

        Parameters:
            extreme_fn (Callable[[list[int]], int]): A function to determine the extreme value.

        Returns:
            int: The number corresponding to the list (index) with the longest non-decreasing sequence.
        """

        grouped_by_non_decreasing_sequence = defaultdict(list)
        all_numbers = self.get_all_numbers()
        for i in range(len(all_numbers)):
            length = Numbers.get_length_of_non_decreasing_sequence(all_numbers[i])
            grouped_by_non_decreasing_sequence[length].append(i)

        extreme_value = extreme_fn(list(grouped_by_non_decreasing_sequence.keys()))
        result = grouped_by_non_decreasing_sequence[extreme_value]
        return result[0] if len(result) == 1 else result

    def find_index_of_extreme_difference(self, extreme_fn: Callable[[list[int]], int]) -> int | list[int]:

        """
        Find the extreme difference between elements of three lists.

        Parameters:
            extreme_fn (Callable[[list[int]], int]): A function to determine the extreme value.

        Returns:
            int | list[int]: The index or indices of the extreme difference(s) between elements of the lists.
                If there's a single index, returns an integer. If multiple indices have the same extreme difference,
                returns a list of integers.
        """

        grouped_by_diff = defaultdict(list)
        for i in range(0, len(self.smallest_numbers)):
            diff = self._calculate_difference_by_index(i)
            grouped_by_diff[diff].append(i)

        extreme_diff = extreme_fn(list(grouped_by_diff.keys()))
        result = grouped_by_diff[extreme_diff]
        return result[0] if len(result) == 1 else result

    def _calculate_difference_by_index(self, index: int) -> int:
        sorted_smallest = sorted(self.smallest_numbers, reverse=True)
        sorted_middle = sorted(self.middle_numbers, reverse=True)
        sorted_highest = sorted(self.highest_numbers, reverse=True)

        diff_1 = abs(sorted_smallest[index] - sorted_middle[index])
        diff_2 = abs(sorted_smallest[index] - sorted_highest[index])
        diff_3 = abs(sorted_middle[index] - sorted_highest[index])
        return diff_1 + diff_2 + diff_3

#
# def main() -> None:
#     # filename = 'data/numbers.txt'
#     # lists = Numbers.from_file(filename)
#     # print(lists)
#     # print("-------------------------(1)-------------------------")
#     # is_file_perfect = lists.is_file_perfect()
#     # print(f'Is file perfect: {is_file_perfect}')
#     lists = Numbers([13, 17, 19, 29, 10],
#                     [28, 25, 58, 60, 49],
#                     [56, 78, 99, 98, 432])
#     # print(lists.find_extreme_non_decreasing_sequence(lambda nums: max(nums)))
#     print(lists.find_index_of_extreme_difference(lambda nums: max(nums)))
#     #
#     # print("-------------------------(2)-------------------------")
#     # diff = lists.get_diff_between(
#     #     lambda nums: max(nums), lambda nums2: min(nums2)
#     # )
#     # print(f'Difference between largest element data from first list and smallest from second list: {diff}')
#     # count = lists.count_elements_meeting_condition(lambda n: n % diff == 0)
#     # print(f'Count of elements divisble by {diff} in the third list: {count}')
#     #
#     # print("-------------------------(3)-------------------------")
#     # longest_non_decreasing_sequence = lists.find_extreme_non_decreasing_sequence(lambda nums: max(nums))
#     # print(f'Longest non decreasing sequence has list data: {longest_non_decreasing_sequence}')
#     # shortest_non_decreasing_sequence = lists.find_extreme_non_decreasing_sequence(lambda nums: min(nums))
#     # print(f'Shortest non decreasing sequence has list data: {shortest_non_decreasing_sequence}')
#     #
#     # print("-------------------------(4)-------------------------")
#     # smallest_diff = lists.find_extreme_difference(lambda nums: min(nums))
#     # largest_diff = lists.find_extreme_difference(lambda nums: max(nums))
#     # print(f'Index at which there is the smallest difference between elements: {smallest_diff}')
#     # print(f'Index at which there is the the largest difference between elements: {largest_diff}')
#     # s = re.match(r'^(\d+;){2}\d+$', '21;2;1')
#     # r = Row.parse('21;2;1')
#     # print(r.numbers)
#
#
# if __name__ == '__main__':
#     main()
