from lessons.lessons.l2.lesson_results import Lesson2Results


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
    for result in lesson_results.check().values():
        assert result


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
    for result in lesson_results.check().values():
        assert not result
