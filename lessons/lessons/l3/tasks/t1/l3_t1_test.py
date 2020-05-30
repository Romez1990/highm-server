def test_check():
    from lessons.lessons.l3.tasks.t1.answer import Answer1
    answers = {
        'x': 0.978,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l3.tasks.t1.answer import Answer1
    answers = {
        'x': 99.978,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == 0
