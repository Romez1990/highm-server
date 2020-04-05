from lessons.load import load_lessons
from lessons.lessons.l1.tasks.t4.answer import Answer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'result': [
            [-147, -68, 137],
            [-41, -65, 48],
            [-96, -82, 45],
        ],
    }
    task = Answer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'result': [
            [-147, -68, 137],
            [-41, -65, 48],
            [-96, -82, 4599],
        ],
    }
    task = Answer(n=1, **answer)
    assert not task.check()
