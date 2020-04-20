from lessons.lessons.l1.tasks.t4.answer import Answer4


def test_check():
    answers = {
        'result': [
            [-147, -68, 137],
            [-41, -65, 48],
            [-96, -82, 45],
        ],
    }
    answer = Answer4(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'result': [
            [-147, -68, 137],
            [-41, -65, 48],
            [-96, -82, 4599],
        ],
    }
    answer = Answer4(n=1, **answers)
    assert not answer.check()
