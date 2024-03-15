import random
import statistics
from dataclasses import dataclass
from collections import defaultdict
from algohub.algorithms.numbers.digits import sum_digits

"""
Zad 1
Przygotuj tablicę kwadratową o dowolnym wymiarze z przedziału <4, 7>
oraz dowolnie losowanych elementach z przedziału <-30, 30>.
a) sprawdź, ile elementów w danym wierszu jest większych co najmniej
o 5 od elementu na przekątnej w tym wierszu, DONE
b) sprawdź, czy elementy na przekątnej począwszy od elementu w
wierszu zerowym tworzą rosnący ciąg arytmetyczny o elementach
dodatnich, DONE
c) wyznacz wiersz, w którym elementy począwszy od kolumny numer zero
tworzą najdłuższy ciąg rosnący o różnicy większej o 3 done

default dictem pogruowac wg dlugosci ciagu rosnacego. Jezeli
od pierwszego elemetnu nie jest rosnacy to dlugosc wynosi 0  

d) wyznacz wiersz, w którym odchylenie standardowe elementów ma
najmniejszą wartość,  DONE

e) najmniejszy element z każdej kolumny zwiększ o największą wartość
z wiersza o tym samym numerze co analizowana kolumna,
tylko wtedy jak rows==columns

1 2 3 4
5 6 7 8

f) utwórz drugą tablicę o tych samych wymiarach, a następnie wyznacz
trzecią tablicę. Trzecia tablica zawiera na każdej pozycji
wartość będącą sumą cyfr elementów z tablicy pierwszej i drugiej
elementów na tej samej pozycji.  done
"""


@dataclass
class MatrixGenerator:
    min_size: int = 4
    max_size: int = 7
    min_val: int = -30
    max_val: int = 30

    @staticmethod
    def draw_number(r_min: int = 10, r_max: int = 20) -> int:
        if r_min > r_max:
            raise ValueError('Incorrect range')
        return random.randint(r_min, r_max)

    def generate_matrix(self) -> list[list[int]]:
        # rows, columns = self.draw_number(self.min_size, self.max_size), random.randint(self.min_size, self.max_size)
        rows = self.draw_number(self.min_size, self.max_size)
        columns = self.draw_number(self.min_size, self.max_size)
        rows = 6
        columns = 7
        return [[self.draw_number(self.min_val, self.max_val) for _ in range(columns)] for _ in range(rows)]


class MatrixAnalysis:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def count_elements_greater_than_diagonal_by(self, row: int, diff: int = 5) -> int:
        if not 0 <= row <= len(self.matrix) - 1:
            raise ValueError("Row out of matrix size")
        diagonal_element = self.matrix[row][row]
        return sum((1 for c in self.matrix[row] if c - diff >= diagonal_element))

    def has_diagonal_arithmetic_sequence(self) -> bool:
        common_diff = self.matrix[1][1] - self.matrix[0][0]

        for i in range(1, len(self.matrix) - 1):
            diff = self.matrix[i + 1][i + 1] - self.matrix[i][i]
            if diff != common_diff:
                return False
        return True

    def get_row_with_highest_sd(self):
        group_by_sd = defaultdict(list)

        for index, row in enumerate(self.matrix):
            sd = statistics.stdev(row)
            group_by_sd[sd].append(index)
        print(group_by_sd.items())
        return max(group_by_sd.items(), key=lambda e: e[0])[1]

    # c) wyznacz wiersz, w którym elementy począwszy od kolumny numer zero
    # tworzą najdłuższy ciąg rosnący o różnicy większej o 3

    # dlugosc ciagu rosnacego dla wiersza. 0 jesli nie jest rosnacy od pierwszego indexu
    def get_row_increasing_sequence_length(self, row: int, diff: int) -> int:
        if not self.matrix[row][1] - self.matrix[row][0] > diff:
            return 0
        count = 1

        for i in range(2, len(self.matrix[row])):
            if self.matrix[row][i] - self.matrix[row][i - 1] > diff:
                count += 1
            else:
                break
        return count

    # Sequence
    def get_row_with_longest_increasing_sequence(self, diff: int):
        grouped_by_sequence = defaultdict(list)

        for i in range(len(self.matrix)):
            count_of_sequence = self.get_row_increasing_sequence_length(i, diff)
            grouped_by_sequence[count_of_sequence].append(i)
            print(grouped_by_sequence.items())
        return max(grouped_by_sequence.items())[1]


class MatrixOperations:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def generate_third_matrix(self, min_val: int, max_val: int):
        second_matrix = [[random.randint(min_val, max_val) for _ in row] for row in self.matrix]
        third_matrix = [[0] * len(row) for row in self.matrix]

        for i in range(len(third_matrix)):
            for j in range(len(third_matrix[i])):
                third_matrix[i][j] = sum_digits(self.matrix[i][j]) + sum_digits(second_matrix[i][j])
        return third_matrix

# def main() -> None:
#     matrix = MatrixGenerator().generate_matrix()
#     for row in matrix:
#         print(row)
#     matrix_analysis = MatrixAnalysis(matrix)
#     print("GREATER THAN DIAGONAL ROW 3")
#     print(matrix_analysis.count_elements_greater_than_diagonal_by(3))
#     print('HAS DIAGONAL ARITHMETIC SEQUENCE')
#     print(matrix_analysis.has_diagonal_arithmetic_sequence())
#     print('ROW WITH HWIGHESR SD')
#     print(matrix_analysis.get_row_with_highest_sd())
#     print("ROW WITH LONGEST INCREASING SEQUENCE")
#     print(matrix_analysis.get_row_with_longest_increasing_sequence(3))
#
#     matrix_operations = MatrixOperations(matrix)
#     print('THIRD MATRIX')
#     print(matrix_operations.generate_third_matrix(-30, 30))
#
#
# if __name__ == '__main__':
#     main()
