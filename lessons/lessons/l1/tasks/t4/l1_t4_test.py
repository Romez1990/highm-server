def test_check():
    from lessons.lessons.l1.tasks.t4.answer import Answer4
    answers = {
        'result': [
            [-147, -68, 137],
            [-41, -65, 48],
            [-96, -82, 45],
        ],
    }
    answer = Answer4(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l1.tasks.t4.answer import Answer4
    answers = {
        'result': [
            [-147, -68, 137],
            [-41, -65, 48],
            [-96, -82, 4599],
        ],
    }
    answer = Answer4(n=1, **answers)
    answer.check()
    assert answer.points == 0
