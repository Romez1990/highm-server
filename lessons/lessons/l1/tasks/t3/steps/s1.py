from typing import List
from numpy import array
from numpy.linalg import det


def check(task):
    return task.determinant == get_determinant(task.matrix_a)


def get_determinant(a: List[List[int]]) -> int:
    return int(round(det(array(a))))
