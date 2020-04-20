from lessons.lessons.l1.tasks.t5.answer import Answer5


def test_check():
    answers = {
        'x1': 0,
        'x2': 1,
    }
    answer = Answer5(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'x1': 0,
        'x2': 199,
    }
    answer = Answer5(n=1, **answers)
    assert not answer.check()
