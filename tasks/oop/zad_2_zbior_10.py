"""
2. W przygotowanym przez Ciebie pliku tekstowym w każdym wierszu umieść
po trzy liczby całkowite oddzielone średnikiem. Postać przykładowego
wiersza to: 32;56;10. Liczba wierszy jest dowolna. Należy przygotować
klasę Listy, która posiada w sobie trzy listy elementów typu
całkowitoliczbowego. Konstruktor klasy pobiera do list dane z pliku
tekstowego o nazwie podanej jako argument konstruktora. Pierwsza lista
przechowuje najmniejsze liczby z poszczególnych wierszy. Druga lista
przechowuje drugie co do wielkości liczby z poszczególnych wierszy.
Trzecia lista przechowuje największe liczby z poszczególnych wierszy.
Umawiamy się, że plik z Twoimi danymi nazywamy doskonałym, jeżeli
pierwsza lista ma wszystkie elementy mniejsze od listy drugiej,
natomiast druga lista ma wszystkie elementy mniejsze od listy trzeciej.
Napisz w klasie Listy metody, które rozwiążą następujące problemy:


->> Sprawdź czy przygotowany przez Ciebie plik jest plikiem doskonałym?
 Które liczby z listy pierwszej oraz które liczby z listy drugiej
należałoby usunąć, żeby zaszedł warunek na plik doskonały? Wykonaj
zestawienie prezentujące te liczby.

->> Wyznacz różnicę pomiędzy największym elementem pierwszej listy oraz
najmniejszym elementem drugiej listy. Ile elementów w trzeciej
liście dzieli się przez tak wyznaczoną różnicę, o ile nie jest ona
zerowa?

->> Wyznacz tą z trzech list w klasie Listy, która posiada w sobie
najdłuższy ciąg niemalejący utworzony z jej elementów. Zwróć słownie
numer wyznaczonej listy jako PIERWSZA, DRUGA lub TRZECIA.

->> Posortuj trzy listy malejąco i sprawdź, dla jakiego indeksu
elementów list różnica pomiędzy elementami trzech list jest
najmniejsza, a dla jakiego indeksu różnica pomiędzy elementami
trzech list jest największa.
"""

from typing import Callable
from collections import defaultdict


class Lists:
    def __init__(self, filename: str):
        self.smallest_numbers = []
        self.middle_numbers = []
        self.highest_numbers = []

        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            numbers = [[int(n) for n in nums.split(';')] for nums in lines]
            self.smallest_numbers = [min(subnumbers) for subnumbers in numbers]
            self.middle_numbers = [sorted(subnumbers)[1] for subnumbers in numbers]
            self.highest_numbers = [max(subnumbers) for subnumbers in numbers]

    def is_file_perfect(self) -> bool | tuple[bool, dict[int, list[int]]]:
        numbers_to_delete = {0: [], 1: []}

        for i in range(len(self.smallest_numbers)):
            for j in range(len(self.middle_numbers)):
                if not self.smallest_numbers[i] < self.middle_numbers[j]:
                    numbers_to_delete[0].append(self.smallest_numbers[i])

        for i in range(len(self.middle_numbers)):
            for j in range(len(self.highest_numbers)):
                if not self.middle_numbers[i] < self.highest_numbers[j]:
                    numbers_to_delete[1].append(self.middle_numbers[i])
        values = [n for n in numbers_to_delete.values() if n]
        return True if not values else (False, numbers_to_delete)

    def get_diff_between(self,
                         finisher_fn_1: Callable[[list[int]], int],
                         finisher_fn_2: Callable[[list[int]], int]) \
            -> int:
        return finisher_fn_1(self.smallest_numbers) - finisher_fn_2(self.middle_numbers)

    def count_elements_divisible_by(self, n: int):
        if n == 0:
            raise ValueError('Can not divide by 0')
        nn = abs(n) if n < 0 else n
        return sum(1 for num in self.highest_numbers if num % nn == 0)

    @staticmethod
    def get_length_of_nondecreasing_sequence(numbers: list[int]):
        if numbers[1] < numbers[0]:
            return 0
        count = 1
        for i in range(2, len(numbers)):
            if numbers[i] >= numbers[i - 1]:
                count += 1
            else:
                break
        return count

    def find_extreme_non_decreasing_sequence(self, extreme_fn: Callable[[list[int]], int]) -> None:
        length_l1 = Lists.get_length_of_nondecreasing_sequence(self.smallest_numbers)
        length_l2 = Lists.get_length_of_nondecreasing_sequence(self.middle_numbers)
        length_l3 = Lists.get_length_of_nondecreasing_sequence(self.highest_numbers)
        extreme_value = extreme_fn([length_l1, length_l2, length_l3])

        if extreme_value == length_l1:
            print('FIRST LIST')
        elif extreme_value == length_l2:
            print('SECOND LIST')
        else:
            print('THIRD LIST')

    def find_extreme_difference(self, extreme_fn: Callable[[list[int]], int]) -> int | list[int]:
        sorted_smallest = sorted(self.smallest_numbers, reverse=True)
        sorted_middle = sorted(self.middle_numbers, reverse=True)
        sorted_highest = sorted(self.highest_numbers, reverse=True)

        grouped_by_diff = defaultdict(list)
        for i in range(0, len(self.smallest_numbers)):
            diff_1 = abs(sorted_smallest[i] - sorted_middle[i])
            diff_2 = abs(sorted_smallest[i] - sorted_highest[i])
            diff_3 = abs(sorted_middle[i] - sorted_highest[i])
            diff = diff_1 + diff_2 + diff_3
            grouped_by_diff[diff].append(i)

        extreme_diff = extreme_fn(list(grouped_by_diff.keys()))
        result = grouped_by_diff[extreme_diff]
        return result[0] if len(result) == 1 else result


def main() -> None:
    filename = 'data/app_2_numbers.txt'
    lists = Lists(filename)
    print(lists.smallest_numbers)
    print(lists.middle_numbers)
    print(lists.highest_numbers)
    nums = [1, 0, 1, 1, 1, 0]
    print(lists.get_length_of_nondecreasing_sequence(nums))
    print(lists.find_extreme_non_decreasing_sequence(lambda numbers: max(numbers)))
    print(lists.find_extreme_difference(lambda numbers: min(numbers)))


if __name__ == '__main__':
    main()
