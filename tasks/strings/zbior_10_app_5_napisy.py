import re
from typing import Callable

"""
Napisz program, w którym pobierasz od użytkownika napis, dopóki nie będzie posiadał
na przemian dużej litery oraz cyfry. Przykładem napisu, który spełnia to kryterium, jest A9B3C7.
Należy na podstawie pobranego napisu wygenerować nowy napis, w którym zastąpisz cyfrę liczbami,
które są dzielnikami kodu ASCII znaku poprzedzającego cyfrę większymi od tej cyfry. Przykładowo dla napisu B3 wynikiem
jest B611223366, ponieważ litera B ma kod ASCII 66. Dzielnikami liczby 66 są: 1, 2, 3, 6, 11, 22, 33, 66.
 Dzielniki większe od 3 to 6, 11, 22, 33, 66 i to one zastępują cyfrę 3 w napisie.
"""


def get_string_until(message: str, condition_fn: Callable[[str], bool]) -> str:
    while not condition_fn(v := input(f'{message}:\n')):
        pass
    return v


def get_divisors(n: int) -> list[int] | float:
    if n == 0:
        return float('inf')
    nn = abs(n) if n < 0 else n
    divisors = {1: 1, 2: [1, 2], 3: [1, 3]}
    if nn in divisors:
        return divisors[n]

    divisors_list = [1]
    i = 2
    while i * i < nn:
        if nn % i == 0:
            divisors_list.extend([i, nn // i])
        i += 1
    if i * i == nn:
        divisors_list.append(i)
    return sorted(divisors_list + [n])


def replace_digits_with_divisors(text: str) -> str:
    items = []
    for i in range(1, len(text), 2):
        digit = int(text[i])
        char = text[i - 1]
        char_code = ord(char)
        divisors = [d for d in get_divisors(char_code) if d > digit]
        items.extend([char] + divisors)
    return ''.join(str(i) for i in items)


def does_string_match_regex(text: str, regex: str = r'^([A-Z]\d)+$') -> bool:
    if not re.match(regex, text):
        return False
    return True
