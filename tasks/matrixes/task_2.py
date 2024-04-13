from dataclasses import dataclass, field
import random
from typing import Callable

"""
4. Napisz program, w którym przygotujesz tablicę jednowymiarową liczb
całkowitych. Wymiar tablicy jest losowany z przedziału <10, 20>.
Elementy tablicy losowane są z przedziału <200, 560>. Posortuj elementy
tablicy malejąco według sumy cyfr tych elementów. Następnie oblicz
średnią arytmetyczną wszystkich elementów w tablicy. Wygeneruj tablicę
dwuwymiarową, która posiada dokładnie 3 wiersze oraz tyle kolumn ile
tablica jednowymiarowa. Pierwszy wiersz w tej tablicy, to elementy
tablicy jednowymiarowej pomniejszone o wartość całkowitej części
średniej arytmetycznej. Drugi wiersz to elementy tablicy
jednowymiarowej. Trzeci wiersz to elementy tablicy jednowymiarowej
"""


@dataclass
class ArrayGenerator:
    """
    Generates a one-dimensional list of random integers.

    Attributes:
        min_size (int): The minimum size of the generated array. Default is 10.
        max_size (int): The maximum size of the generated array. Default is 20.
        min_val (int): The minimum value for the elements in the generated array. Default is 200.
        max_val (int): The maximum value for the elements in the generated array. Default is 560.
    """

    min_size: int = 10
    max_size: int = 20
    min_val: int = 200
    max_val: int = 560

    def generate_array(self) -> list[int]:
        """
        Generates a one-dimensional list of random integers.

        Returns:
            list[int]: A one-dimensional list of random integers.
        """

        size = random.randint(self.min_size, self.max_size)
        return [random.randint(self.min_val, self.max_val) for _ in range(size)]


@dataclass
class ArrayProcessor:
    """
    Processes operations on arrays.

    Attributes:
        numbers (list[int]): List of integers.

    """

    numbers: list[int] = field(default_factory=list)

    def sort_numbers(self, sorting_fn: Callable[[int], int]) -> list[int]:
        """
         Sorts the list based on a given sorting function.

         Parameters:
             sorting_fn (Callable[[int], int]): The sorting function.

         Returns:
             list[int]: A sorted array.
         """

        return sorted(self.numbers, key=lambda n: sorting_fn(n), reverse=True)

    def calculate_average(self) -> int:
        """
        Calculates the average of the elements in the list.

        Returns:
            int: The average of the elements in the list.
        """

        return sum(self.numbers) // len(self.numbers)


@dataclass
class ArrayTransformer:
    """
    Transforms a list into a two-dimensional matrix.

    Attributes:
        numbers (list[int]): List of integers.
    """

    numbers: list[int] = field(default_factory=list)

    def generate_matrix(self, rows: int = 3) -> list[list[int]]:
        """
         Generates a two-dimensional matrix.

         Parameters:
             rows (int): Number of rows in the matrix.

         Returns:
             list[list[int]]: A two-dimensional matrix.
         """

        matrix = [[n for n in self.numbers] for _ in range(rows)]
        avg = ArrayProcessor(self.numbers).calculate_average()
        matrix[0] = [n - avg for n in self.numbers]
        return matrix
