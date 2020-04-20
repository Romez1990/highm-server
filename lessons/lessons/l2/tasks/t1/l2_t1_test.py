from lessons.lessons.l2.tasks.t1.answer import Answer1


def test_check():
    answers = {
        'x': 0,
        'y': -1,
        'z': 1,
    }
    answer = Answer1(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'x': 0,
        'y': -1,
        'z': 199,
    }
    answer = Answer1(n=1, **answers)
    assert not answer.check()
