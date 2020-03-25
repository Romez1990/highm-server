from .task import Task


def test_check():
    answer = {
        "product": [
            [-4, 1],
            [-12, 3]
        ],
        "trace": "20",
    }
    task = Task(n=1, **answer)
    assert task.check()
