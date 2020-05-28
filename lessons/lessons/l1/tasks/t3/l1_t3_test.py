def test_check():
    from lessons.lessons.l1.tasks.t3.answer import Answer3
    answers = {
        'determinant': 264,
    }
    answer = Answer3(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l1.tasks.t3.answer import Answer3
    answers = {
        'determinant': 26499,
    }
    answer = Answer3(n=1, **answers)
    answer.check()
    assert answer.points == 0
