from os import getenv
from typing import Union
from dotenv import load_dotenv

load_dotenv()


def env(key: str, type_: type = str) -> Union[str, int, bool]:
    value = getenv(key)
    if value is None:
        raise EnvironmentError(f'no key {key} in .env file')
    if type_ is str:
        return value
    if type_ is int:
        return int(value)
    if type_ is bool:
        return to_bool(value, key)
    raise ValueError(f'type {type_} is unacceptable')


def to_bool(value: str, key: str) -> bool:
    value = value.lower()
    if value == 'true':
        return True
    if value == 'false':
        return False
    raise EnvironmentError(f'key {key} can only be true or false')
