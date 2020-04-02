from typing import List


def get_matrix_a(n: int) -> List[List[int]]:
    return [
        [1, 2, n - 15],
        [n - 10, 0, 4],
        [2, 1, 7],
    ]
