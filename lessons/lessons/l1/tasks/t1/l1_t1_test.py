from lessons.lessons.l1.tasks.t1.answer import Answer1


def test_check():
    answers = {
        'which_of_products': 'AB',
        'product': [
            [-4, 1, 4],
            [-12, 3, 13],
        ]
    }
    answer = Answer1(n=1, **answers)
    assert answer.check()


def test_check_fail():
    answers = {
        'which_of_products': 'AB',
        'product': [
            [-4, 1, 4],
            [-12, 3, 1399],
        ]
    }
    answer = Answer1(n=1, **answers)
    assert not answer.check()
