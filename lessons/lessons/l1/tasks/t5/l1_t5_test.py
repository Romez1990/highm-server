def test_check():
    from lessons.lessons.l1.tasks.t5.answer import Answer5
    answers = {
        'x1': 0,
        'x2': 1,
    }
    answer = Answer5(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l1.tasks.t5.answer import Answer5
    answers = {
        'x1': 0,
        'x2': 199,
    }
    answer = Answer5(n=1, **answers)
    answer.check()
    assert answer.points == 0
