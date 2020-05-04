from lessons.lessons.l1.tasks.t2.answer import Answer2


def test_check():
    answers = {
        'product': [
            [-35, -62],
            [-279, -190],
        ],
        'trace': -225,
    }
    answer = Answer2(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'product': [
            [-35, -62],
            [-279, -190],
        ],
        'trace': -22599,
    }
    answer = Answer2(n=1, **answers)
    assert not answer.check()
