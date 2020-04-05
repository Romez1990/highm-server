from lessons.load import load_lessons
from lessons.lessons.l1.tasks.t1.answer import Answer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'which_of_products': 'AB',
        'product': [
            [-4, 1, 4],
            [-12, 3, 13],
        ]
    }
    task = Answer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'which_of_products': 'AB',
        'product': [
            [-4, 1, 4],
            [-12, 3, 1399],
        ]
    }
    task = Answer(n=1, **answer)
    assert not task.check()
