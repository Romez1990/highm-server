# HighM server
Backend for [HighM project](https://github.com/Romez1990/highm).

HighM is web application for college to organize math lessons.

## Getting started
These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes. See deployment for notes on
how to deploy the project on a live system.

### Prerequisites
What things you need to have globally installed:
- Python 3.8 or higher
- Pipenv
- PostgreSQL
- libpq-dev (only for Linux)

### Installing
Install project dependencies.
```shell script
pipenv install
```

Run database migrations.
```shell script
pipenv run python manage.py migrate
```

Copy .env.example to .env. Set DEBUG=False for production, specify server
host, client url, database and email credentials.
```shell script
cp .env.example .env
```
Or instead of .env file you can set environment variables.

Run development server.
```shell script
pipenv run python manage.py runserver
```

To create a user you should add a row to auth_user table with email and add a
row to account_emailaddress with corresponding email.

You can also login to Django REST Framework panel with username and password
only in development mode

## Automated testing
To run all the automated tests
```shell script
pipenv run test
```

### Unit tests
Unit tests test every module individually
```shell script
pipenv run unit-test
```
