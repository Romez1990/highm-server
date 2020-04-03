from lessons.load import load_lessons
from lessons.lessons.l1.tasks.t2.task_answer import TaskAnswer


def setup_module() -> None:
    load_lessons()


def test_check():
    answer = {
        'product': [
            [-35, -62],
            [-279, -190],
        ],
        'trace': -225,
    }
    task = TaskAnswer(n=1, **answer)
    assert task.check()


def test_check_fail():
    answer = {
        'product': [
            [-35, -62],
            [-279, -190],
        ],
        'trace': -22599,
    }
    task = TaskAnswer(n=1, **answer)
    assert not task.check()
