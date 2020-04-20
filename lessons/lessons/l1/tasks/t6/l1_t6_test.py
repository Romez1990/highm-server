from lessons.lessons.l1.tasks.t6.answer import Answer6


def test_check():
    answers = {
        'determinant': 227,
    }
    answer = Answer6(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'determinant': 22799,
    }
    answer = Answer6(n=1, **answers)
    assert not answer.check()
