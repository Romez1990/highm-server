from .task import Task


def test_check():
    answer = {
        "which_of_products": "AB",
        "product": [
            [-4, 1, 4],
            [-12, 3, 13]
        ]
    }
    task = Task(n=1, **answer)
    assert task.check()
