def test_check():
    from lessons.lessons.l2.tasks.t2.answer import Answer2
    answers = {
        'x': 2,
        'y': -3,
        'z': 1,
    }
    answer = Answer2(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l2.tasks.t2.answer import Answer2
    answers = {
        'x': 2,
        'y': -3,
        'z': 199,
    }
    answer = Answer2(n=1, **answers)
    answer.check()
    assert answer.points == 0
