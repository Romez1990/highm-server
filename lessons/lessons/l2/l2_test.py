def test_check():
    from lessons.lessons.l2.lesson_answers import Lesson2Answers
    answers = {
        'answer1': {
            'x': 0,
            'y': -1,
            'z': 1,
        },
        'answer2': {
            'x': 2,
            'y': -3,
            'z': 1,
        },
    }
    lesson_answers = Lesson2Answers(n=1, **answers)
    lesson_answers.check()
    assert lesson_answers.points == lesson_answers.max_points()


def test_check_fail():
    from lessons.lessons.l2.lesson_answers import Lesson2Answers
    answers = {
        'answer1': {
            'x': 0,
            'y': -1,
            'z': 199,
        },
        'answer2': {
            'x': 2,
            'y': -3,
            'z': 199,
        },
    }
    lesson_answers = Lesson2Answers(n=1, **answers)
    lesson_answers.check()
    assert lesson_answers.points == 0
