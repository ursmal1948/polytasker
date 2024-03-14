import random
from tasks.common_functions import get_array_length

"""
Wspólny rozmiar dwóch tablic jednowymiarowych o elementach typu int jest losowany
z przedziału <3, 11>. Elementy tablic są losowane z przedziału <0,9>. Znajdź najdłuższy
wspólny podciąg liczb występujący w dwóch tablicach. Wypisz wszystkie liczby tego podciągu
słownie. Przykładowo, jeżeli mamy dwie tablice o elementach: 1 2 3 4 5 6 oraz 3 4 5 6 7 8 to najdłuższym wspólnym
podciągiem tych tablic jest 3 4 5 6, czyli słownie na ekranie powinno wyświetlić się: trzy, cztery, pięć, sześć.
"""


def gemerate_n_numbers(size: int, r_min: int, r_max: int) -> list[int]:
    if r_min > r_max:
        raise ValueError('Incorrect range')
    return [random.randint(r_min, r_max) for _ in range(size)]


def get_lcs(nums1: list[int], nums2: list[int]) -> list[int]:
    if nums1 == nums2:
        return nums1
    for i in range(len(nums1)):
        pass


def main() -> None:
    array_length = get_array_length(3, 11)
    v_min = 0
    v_max = 9
    numbers1 = gemerate_n_numbers(array_length, v_min, v_max)
    numbers2 = gemerate_n_numbers(array_length, v_min, v_max)


if __name__ == '__main__':
    main()
