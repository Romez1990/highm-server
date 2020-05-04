from lessons.lessons.l1.lesson import Lesson1Results


def test_check():
    answers = {
        'answer1': {
            'which_of_products': 'AB',
            'product': [
                [-4, 1, 4],
                [-12, 3, 13],
            ],
        },
        'answer2': {
            'product': [
                [-35, -62],
                [-279, -190],
            ],
            'trace': -225,
        },
        'answer3': {
            'determinant': 264,
        },
        'answer4': {
            'result': [
                [-147, -68, 137],
                [-41, -65, 48],
                [-96, -82, 45],
            ]
        },
        'answer5': {
            'x1': 0,
            'x2': 1,
        },
        'answer6': {
            'determinant': 227,
        }
    }
    lesson_results = Lesson1Results(n=1, **answers)
    [assert_true(result) for result in lesson_results.check().values()]


def test_check_fail():
    answers = {
        'answer1': {
            'which_of_products': 'AB',
            'product': [
                [-4, 1, 4],
                [-12, 3, 1399],
            ],
        },
        'answer2': {
            'product': [
                [-35, -62],
                [-279, -190],
            ],
            'trace': -22599,
        },
        'answer3': {
            'determinant': 26499,
        },
        'answer4': {
            'result': [
                [-147, -68, 137],
                [-41, -65, 48],
                [-96, -82, 4599],
            ]
        },
        'answer5': {
            'x1': 0,
            'x2': 199,
        },
        'answer6': {
            'determinant': 22799,
        }
    }
    lesson_results = Lesson1Results(n=1, **answers)
    [assert_false(result) for result in lesson_results.check().values()]


def assert_true(result: bool) -> None:
    assert result


def assert_false(result: bool) -> None:
    assert not result
