from lessons.base import (
    LessonBaseBase,
    LessonBasicBase,
    LessonBase,
)


class Lesson1BasicBase(LessonBaseBase):
    title = 'Выполнение действий с матрицами. Вычисление определителя матрицы.'


class Lesson1Basic(Lesson1BasicBase, LessonBasicBase):
    pass


class Lesson1(Lesson1BasicBase, LessonBase):
    goals = [
        'получить навыки выполнения операций над матрицами и вычисления '
        'определителей квадратных матриц различных порядков',
        'закрепить теоретические и практические знания и навыки по данной теме',
    ]
