def test_check():
    from lessons.lessons.l1.tasks.t1.answer import Answer1
    answers = {
        'which_of_products': 'AB',
        'product': [
            [-4, 1, 4],
            [-12, 3, 13],
        ]
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l1.tasks.t1.answer import Answer1
    answers = {
        'which_of_products': 'BA',
        'product': [
            [-4, 1, 4],
            [-12, 3, 1399],
        ]
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == 0
