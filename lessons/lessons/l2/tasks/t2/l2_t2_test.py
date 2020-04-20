from lessons.lessons.l2.tasks.t2.answer import Answer2


def test_check():
    answers = {
        'x': 2,
        'y': -3,
        'z': 1,
    }
    answer = Answer2(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'x': 2,
        'y': -3,
        'z': 199,
    }
    answer = Answer2(n=1, **answers)
    assert not answer.check()
