def test_check():
    from lessons.lessons.l3.lesson_answers import Lesson3Answers
    answers = {
        'answer1': {
            'x': 0.978,
        },
    }
    lesson_answers = Lesson3Answers(n=1, **answers)
    lesson_answers.check()
    assert lesson_answers.points == lesson_answers.max_points()


def test_check_fail():
    from lessons.lessons.l3.lesson_answers import Lesson3Answers
    answers = {
        'answer1': {
            'x': 99.978,
        },
    }
    lesson_answers = Lesson3Answers(n=1, **answers)
    lesson_answers.check()
    assert lesson_answers.points == 0
