from lessons.load import load_lessons
from lessons.lessons.l1.tasks.t5.task_answer import TaskAnswer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'x1': 0,
        'x2': 1,
    }
    task = TaskAnswer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'x1': 0,
        'x2': 199,
    }
    task = TaskAnswer(n=1, **answer)
    assert not task.check()
