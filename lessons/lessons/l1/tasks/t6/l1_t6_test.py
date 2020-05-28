def test_check():
    from lessons.lessons.l1.tasks.t6.answer import Answer6
    answers = {
        'determinant': 227,
    }
    answer = Answer6(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l1.tasks.t6.answer import Answer6
    answers = {
        'determinant': 22799,
    }
    answer = Answer6(n=1, **answers)
    answer.check()
    assert answer.points == 0
