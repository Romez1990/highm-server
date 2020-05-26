grades = [
    # (grade, min_percent)
    (5, 0.90),
    (4, 0.70),
    (3, 0.50),
    (2, 0.0),
]


def get_grade(percent_correct: float) -> int:
    for grade, min_percent in grades:
        if percent_correct >= min_percent:
            return grade
