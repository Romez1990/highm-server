def test_check():
    from lessons.lessons.l4.tasks.t1.answer import Answer1
    answers = {
        'intermediate_results': [
            {'x': 0.10, 'y': 0.95310},
            {'x': 0.25, 'y': 0.89257},
            {'x': 0.40, 'y': 0.84118},
            {'x': 0.55, 'y': 0.79683},
            {'x': 0.70, 'y': 0.75804},
            {'x': 0.85, 'y': 0.72375},
            {'x': 1.00, 'y': 0.69315},
            {'x': 1.15, 'y': 0.66562},
            {'x': 1.30, 'y': 0.64070},
            {'x': 1.45, 'y': 0.61799},
            {'x': 1.60, 'y': 0.59719},
        ],
        'result': 1.11075,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == answer.max_points()


def test_check_fail():
    from lessons.lessons.l4.tasks.t1.answer import Answer1
    answers = {
        'intermediate_results': [
            {'x': 0.10, 'y': 0.95310},
            {'x': 0.25, 'y': 0.89257},
            {'x': 0.40, 'y': 0.84118},
            {'x': 0.55, 'y': 0.79683},
            {'x': 0.70, 'y': 0.75804},
            {'x': 0.85, 'y': 0.72375},
            {'x': 1.00, 'y': 0.69315},
            {'x': 1.15, 'y': 0.66562},
            {'x': 1.30, 'y': 0.64070},
            {'x': 1.45, 'y': 0.61799},
            {'x': 99.60, 'y': 9.59719},
        ],
        'result': 99.11075,
    }
    answer = Answer1(n=1, **answers)
    answer.check()
    assert answer.points == 0
