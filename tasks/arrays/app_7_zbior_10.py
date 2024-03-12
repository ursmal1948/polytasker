import random
from collections import OrderedDict
from tasks.arrays.common_functions import get_array_length

"""
7. Napisz program, w którym wygenerujesz tablicę jednowymiarową liczb
całkowitych. Rozmiar tablicy jest losowany z przedziału <10, 20>,
natomiast elementy tablicy są losowane z przedziału <100, 999>.
Następnie na podstawie utworzonej wcześniej tablicy wygeneruj nową
tablicę, która zawiera w sobie cyfry wszystkich liczb tablicy
pierwszej, ale bez powtórzeń. Przykładowo dla tablicy o elementach:
123, 345, 567 wynikiem jest tablica o elementach: 1, 2, 3, 4, 5, 6, 7.
"""


def generate_array(size: int, r_min: int, r_max: int) -> list[int]:
    if r_min > r_max:
        raise ValueError("Min value is greater than max value=")
    return [random.randint(r_min, r_max) for _ in range(size)]


def get_unique_digits(numbers: list[int]) -> list[int]:
    unique_digits = OrderedDict.fromkeys(int(d) for number in numbers for d in str(number))
    return list(unique_digits)
