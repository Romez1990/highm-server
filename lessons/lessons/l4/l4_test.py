def test_check():
    from lessons.lessons.l4.lesson_answers import Lesson4Answers
    answers = {
        'answer1': {
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
        },
        'answer2': {
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
        },
    }
    lesson_answers = Lesson4Answers(n=1, **answers)
    lesson_answers.check()
    assert lesson_answers.points == lesson_answers.max_points()


def test_check_fail():
    from lessons.lessons.l4.lesson_answers import Lesson4Answers
    answers = {
        'answer1': {
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
        },
        'answer2': {
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
        },
    }
    lesson_answers = Lesson4Answers(n=1, **answers)
    lesson_answers.check()
    assert lesson_answers.points == 0
