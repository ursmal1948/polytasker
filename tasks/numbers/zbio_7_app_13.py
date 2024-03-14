from tasks.common_functions import generate_n_numbers

"""
W pliku tekstowym zapisano obok siebie 101 cyfr z przedziału <0,9>.
Zlicz, ile cyfr w pliku należy zamienić na 1 lub zero, żeby otrzymać
liczbę Googol. Liczba Googol to liczba składająca się z 1 na początku
i stu zer, czyli 10 ^ 100.
"""


def read_from_file(filename: str) -> list[int]:  # app_13_googol
    with open(filename, "r") as f:
        return [int(n) for n in f.readline()]


def count_changes_to_form_googol_number(numbers: list[int]):
    """
    Counts the number of changes needed in a list of integers to form a Googol number
    :param numbers: list[int] a list of integers representing digits
    :return int: the number of changes needed to form a Googol number, where a Googol is defined as a number
     with '1' followed by 100 '0'
    """

    non_zero_digits_count = sum([1 for i in range(1, len(numbers)) if numbers[i] != 0])
    return non_zero_digits_count + (1 if numbers[0] != 1 else 0)
