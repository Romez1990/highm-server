def get_n(request) -> int:
    return request.user.student.n


class StudentNDefault:
    requires_context = True

    def __call__(self, serializer_field):
        request = serializer_field.context['request']
        return get_n(request)
