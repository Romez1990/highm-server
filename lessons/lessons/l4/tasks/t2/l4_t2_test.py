def test_check():
    from lessons.lessons.l4.tasks.t2.answer import Answer2
    answers = {
        'intermediate_results': [
            {'x': 0.1000, 'y': 0.00000},
            {'x': 0.2875, 'y': 0.43301},
            {'x': 0.4750, 'y': 0.61237},
            {'x': 0.6625, 'y': 0.75000},
            {'x': 0.8500, 'y': 0.86603},
            {'x': 1.0375, 'y': 0.96825},
            {'x': 1.2250, 'y': 1.06066},
            {'x': 1.4125, 'y': 1.14564},
            {'x': 1.6000, 'y': 1.22474},
        ],
        'result': 1.20906,
    }
    answer = Answer2(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l4.tasks.t2.answer import Answer2
    answers = {
        'intermediate_results': [
            {'x': 0.1000, 'y': 0.00000},
            {'x': 0.2875, 'y': 0.43301},
            {'x': 0.4750, 'y': 0.61237},
            {'x': 0.6625, 'y': 0.75000},
            {'x': 0.8500, 'y': 0.86603},
            {'x': 1.0375, 'y': 0.96825},
            {'x': 1.2250, 'y': 1.06066},
            {'x': 1.4125, 'y': 1.14564},
            {'x': 99.6000, 'y': 99.22474},
        ],
        'result': 99.20906,
    }
    answer = Answer2(n=1, **answers)
    answer.check()
    assert answer.points == 0
