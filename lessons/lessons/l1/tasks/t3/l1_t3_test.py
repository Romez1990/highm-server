from lessons.lessons.l1.tasks.t3.answer import Answer3


def test_check():
    answers = {
        'determinant': 264,
    }
    answer = Answer3(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'determinant': 26499,
    }
    answer = Answer3(n=1, **answers)
    assert not answer.check()
