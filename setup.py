from setuptools import setup

setup(
    name='flake8-future-division',
    description=(
        'A flake8 plugin to check for use of division without a '
        '__future__.division import'),
    version='0.1',
    py_modules=['flake8_division'],
    entry_points={'flake8.extension': ['F48 = flake8_division:CheckDivision']},
)
