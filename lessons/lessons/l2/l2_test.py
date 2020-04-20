from lessons.lessons.l2.lesson import Lesson2Results


def test_check():
    answers = {
        'answer1': {
            'x': 0,
            'y': -1,
            'z': 1,
        },
        'answer2': {
            'x': 2,
            'y': -3,
            'z': 1,
        },
    }
    lesson_results = Lesson2Results(n=1, **answers)
    [assert_true(result) for result in lesson_results.check().values()]


def test_check_fail():
    answers = {
        'answer1': {
            'x': 0,
            'y': -1,
            'z': 199,
        },
        'answer2': {
            'x': 2,
            'y': -3,
            'z': 199,
        },
    }
    lesson_results = Lesson2Results(n=1, **answers)
    [assert_false(result) for result in lesson_results.check().values()]


def assert_true(result: bool) -> None:
    assert result


def assert_false(result: bool) -> None:
    assert not result
