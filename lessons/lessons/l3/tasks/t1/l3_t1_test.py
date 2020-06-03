def test_check():
    from lessons.lessons.l3.tasks.t1.answer import Answer1
    answers = {
        'x': 0.977913,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_tolerance():
    from lessons.lessons.l3.tasks.t1.answer import Answer1
    answers = {
        'x': 0.97791,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points() - 1
    answers = {
        'x': 0.9779,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points() - 2
    answers = {
        'x': 0.977,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points() - 3


def test_check_fail():
    from lessons.lessons.l3.tasks.t1.answer import Answer1
    answers = {
        'x': 99.977913,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == 0
