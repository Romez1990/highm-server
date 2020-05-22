grades = [
    # (grade, min_percent)
    (5, 0.90),
    (4, 0.70),
    (3, 0.50),
    (2, 0.0),
]


def get_grade(percent_right: float) -> int:
    for grade, min_percent in grades:
        if percent_right > min_percent:
            return grade
