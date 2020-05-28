from pytest import fixture
from django import setup as django_setup


@fixture(autouse=True, scope='session')
def setup():
    django_setup()
