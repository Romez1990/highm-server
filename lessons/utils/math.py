from typing import (
    TypeVar,
    List,
)

T = TypeVar('T')
Matrix = List[List[T]]

MatrixInt = List[List[int]]
MatrixStr = List[List[str]]
MatrixFloat = List[List[float]]

# this is because of a bug in pycharm
# is that correct?
a: Matrix[int] = [
    [1, 2],
    [3, 4],
]


def number_to_expression(number: int, first: bool = False) -> str:
    if not first and number >= 0:
        return f'+{number}'
    return str(number)
