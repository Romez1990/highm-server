def test_check():
    from lessons.lessons.l2.tasks.t1.answer import Answer1
    answers = {
        'x': 0,
        'y': -1,
        'z': 1,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l2.tasks.t1.answer import Answer1
    answers = {
        'x': 0,
        'y': -1,
        'z': 199,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == 0
