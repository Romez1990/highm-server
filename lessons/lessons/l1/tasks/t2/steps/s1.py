from typing import List
from numpy import array
from numpy.linalg import matrix_power


def check(task):
    return task.product == get_product(task.matrix_a)


def get_product(a: List[List[int]]) -> List[List[int]]:
    return matrix_power(array(a), 3).tolist()
