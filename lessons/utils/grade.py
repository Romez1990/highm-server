grades = [
    # (grade, min_percent)
    (5, 90),
    (4, 70),
    (3, 50),
    (2, 0),
]


def get_grade(percent_correct: float) -> int:
    for grade, min_percent in grades:
        if percent_correct >= min_percent:
            return grade
