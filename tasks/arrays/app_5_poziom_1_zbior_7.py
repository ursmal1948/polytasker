import random
from typing import Callable
from collections import defaultdict

"""
Pobierz od użytkownika rozmiar R tablicy jednowymiarowej o elementach
typu int, a następnie losuj do tablicy elementy z przedziału <0, 2*R>
w taki sposób, żeby żaden element tablicy się nie powtórzył. Wyznacz
największą oraz najmniejszą wartość spośród elementów w tablicy oraz
element tablicy o najmniejszej sumie cyfr.
"""


class ArrayOperations:
    def __init__(self, size: int = 10):
        self.size = size
        self.numbers = self.generate_numbers()

    def get_numbers(self):
        return self.numbers

    def generate_numbers(self, r_min: int = 0) -> list[int]:
        r_max = 2 * self.size
        unique_elements = set()
        if r_min > r_max:
            raise ValueError('Incorrect range')
        while len(unique_elements) < self.size:
            unique_elements.add(random.randint(r_min, 2 * self.size))
        return list(unique_elements)

    def get_min_max_element(self) -> tuple[int, int]:
        return min(self.numbers), max(self.numbers)

    def get_element_based_on_mapper(self,
                                    mapper_fn: Callable[[int], int] = lambda n: n,
                                    finisher_fn: Callable[[list[int]], int] = max) \
            -> int | list[int]:
        grouped_elements = defaultdict(list)
        for n in self.numbers:
            key_ = mapper_fn(n)
            grouped_elements[key_].append(n)
        extreme_digit = finisher_fn(list(grouped_elements.keys()))
        return grouped_elements[extreme_digit]
