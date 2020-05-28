def test_check():
    from lessons.lessons.l1.tasks.t2.answer import Answer2
    answers = {
        'product': [
            [-35, -62],
            [-279, -190],
        ],
        'trace': -225,
    }
    answer = Answer2(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l1.tasks.t2.answer import Answer2
    answers = {
        'product': [
            [-35, -62],
            [-279, -19099],
        ],
        'trace': -22599,
    }
    answer = Answer2(n=1, **answers)
    answer.check()
    assert answer.points == 0
