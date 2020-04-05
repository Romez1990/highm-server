from lessons.load import load_lessons
from lessons.lessons.l2.tasks.t1.task_answer import TaskAnswer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'x': 0,
        'y': -1,
        'z': 1,
    }
    task = TaskAnswer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'x': 0,
        'y': -1,
        'z': 199,
    }
    task = TaskAnswer(n=1, **answer)
    assert not task.check()
