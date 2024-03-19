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
        self.smallest = []
        self.middle = []
        self.highest = []

        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            numbers = [[int(n) for n in nums.split(';')] for nums in lines]
            self.smallest = [min(subnumbers) for subnumbers in numbers]
            self.middle = [sorted(subnumbers)[1] for subnumbers in numbers]
            self.highest = [max(subnumbers) for subnumbers in numbers]

    def is_file_perfect(self) -> bool | tuple[bool, dict[int, list[int]]]:
        numbers_to_delete = {0: [], 1: []}

        for i in range(len(self.smallest)):
            for j in range(len(self.middle)):
                if not self.smallest[i] < self.middle[j]:
                    numbers_to_delete[0].append(self.smallest[i])

        for i in range(len(self.middle)):
            for j in range(len(self.highest)):
                if not self.middle[i] < self.highest[j]:
                    numbers_to_delete[1].append(self.middle[i])
        values = [n for n in numbers_to_delete.values() if n]
        return True if not values else (False, numbers_to_delete)

    def get_diff_between(self,
                         function_fn_1: Callable[[list[int]], int],
                         function_fn_2: Callable[[list[int]], int]) \
            -> int:
        return function_fn_1(self.smallest) - function_fn_2(self.middle)

    def count_elements_divisible_by_number(self, n: int):
        if n == 0:
            raise ValueError('Can not divide by 0')
        nn = abs(n) if n < 0 else n
        return sum(1 for num in self.highest if num % nn == 0)

    @staticmethod
    def get_length_nondecreasing_sequence(numbers: list[int]):
        if numbers[1] < numbers[0]:
            return 0
        count = 1
        for i in range(2, len(numbers)):
            if numbers[i] >= numbers[i - 1]:
                count += 1
            else:
                break
        return count

    # min max lub tez avg niemalejaca dlugosc ciagu
    def find_extreme_non_decreasing_sequence(self, extreme_fn: Callable[[list[int]], int]) -> None:
        length_l1 = Lists.get_length_nondecreasing_sequence(self.smallest)
        length_l2 = Lists.get_length_nondecreasing_sequence(self.middle)
        length_l3 = Lists.get_length_nondecreasing_sequence(self.highest)
        extreme_value = extreme_fn([length_l1, length_l2, length_l3])

        if extreme_value == length_l1:
            print('FIRST LIST')
        elif extreme_value == length_l2:
            print('SECOND LIST')
        else:
            print('THIRD LIST')

    def find_min_max_index_difference(self) -> tuple[int, int]:

        sorted_smallest = sorted(self.smallest, reverse=True)
        sorted_middle = sorted(self.middle, reverse=True)
        sorted_highest = sorted(self.highest, reverse=True)

        grouped_by_diff = defaultdict(int)
        for i in range(0, len(self.smallest)):
            diff_1 = abs(sorted_smallest[i] - sorted_middle[i])
            diff_2 = abs(sorted_smallest[i] - sorted_highest[i])
            diff_3 = abs(sorted_middle[i] - sorted_highest[i])
            diff = diff_1 + diff_2 + diff_3
            grouped_by_diff[i] = diff

        smallest_diff = min(grouped_by_diff.items(), key=lambda e: e[1])[0]  # index 4: 92
        highest_diff = max(grouped_by_diff.items(), key=lambda e: e[1])[0]  # index 0: 824
        return smallest_diff, highest_diff


def main() -> None:
    filename = 'data/app_2_numbers.txt'
    lists = Lists(filename)
    print(lists.smallest)
    print(lists.middle)
    print(lists.highest)
    nums = [1, 0, 1, 1, 1, 0]
    print(lists.get_length_nondecreasing_sequence(nums))
    print(lists.find_extreme_non_decreasing_sequence(lambda numbers: max(numbers)))
    print(lists.find_min_max_index_difference())


if __name__ == '__main__':
    main()
