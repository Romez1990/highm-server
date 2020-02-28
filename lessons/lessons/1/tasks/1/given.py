from typing import List


def get_matrix_a(n: int) -> List[List[int]]:
    return [
        [1, n],
        [3, 4],
    ]


def get_matrix_b(n: int) -> List[List[int]]:
    return [
        [n - 5, 1, 3],
        [0, 0, 1],
    ]
