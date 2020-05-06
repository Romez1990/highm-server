from django.core.validators import RegexValidator

group_name_regex = r'^([1-4])([А-Яа-я]{2,4})-(\d{1,2})(а?)\.(\d{2})$'

group_name_validator = RegexValidator(group_name_regex,
                                      'Group name does not match rules.')

registration_code_regex = r'^c\d{6}$'

registration_code_validator = RegexValidator(registration_code_regex,
                                             'Wrong registration code.')
