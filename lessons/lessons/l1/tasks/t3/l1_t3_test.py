from lessons.load import load_lessons
from lessons.lessons.l1.tasks.t3.answer import Answer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'determinant': 264,
    }
    task = Answer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'determinant': 26499,
    }
    task = Answer(n=1, **answer)
    assert not task.check()
