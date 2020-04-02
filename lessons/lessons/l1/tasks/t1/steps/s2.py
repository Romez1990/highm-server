from typing import List
from numpy import array, dot


def check(task):
    return task.product == get_product(task.matrix_a, task.matrix_b)


def get_product(
        a: List[List[int]],
        b: List[List[int]]
) -> List[List[int]]:
    return dot(array(a), array(b)).tolist()
