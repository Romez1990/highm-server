from lessons.load import load_lessons
from lessons.lessons.l1.tasks.t3.task_answer import TaskAnswer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'determinant': 264,
    }
    task = TaskAnswer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'determinant': 26499,
    }
    task = TaskAnswer(n=1, **answer)
    assert not task.check()
