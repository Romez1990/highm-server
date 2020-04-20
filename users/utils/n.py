from rest_framework.request import Request


def get_n(request: Request) -> int:
    user = request.user
    n = user.student.n
    return n
