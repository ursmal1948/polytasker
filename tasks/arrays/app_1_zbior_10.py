from tasks.common_functions import get_array_length

"""
1. Przygotuj tablicę jednowymiarową liczb całkowitych. Wymiar tablicy
jest losowany z przedziału <10, 100>. Każdy element tablicy ma wartość,
którą losujemy z przedziału <100, 200> dopóki suma cyfr nie będzie
liczbą posiadającą dokładnie dwa dzielniki, nie licząc 1 oraz tej
liczby. Wyznacz sumę czterech największych elementów tablicy. Uwaga,
kiedy w tablicy mamy przykładowo elementy: 1 1 1 2 2 2 3 3 4 4 5 5
to cztery największe elementy przyjmujemy jako 5, 4, 3 oraz 2.
"""


def main() -> None:
    array_length = get_array_length(10, 100)


if __name__ == '__main__':
    main()
