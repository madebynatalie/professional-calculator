"""Tests for arithmetic operation classes."""

import pytest

from app.operation import Addition, Division, Multiplication, Operation, Subtraction


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (2, 3, 5),
        (-2, 3, 1),
        (0, 0, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_addition(first_number, second_number, expected):
    operation = Addition()

    assert operation.execute(first_number, second_number) == expected


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (5, 3, 2),
        (3, 5, -2),
        (0, 0, 0),
        (5.5, 2.5, 3.0),
    ],
)
def test_subtraction(first_number, second_number, expected):
    operation = Subtraction()

    assert operation.execute(first_number, second_number) == expected


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 100, 0),
        (2.5, 2, 5.0),
    ],
)
def test_multiplication(first_number, second_number, expected):
    operation = Multiplication()

    assert operation.execute(first_number, second_number) == expected


@pytest.mark.parametrize(
    "first_number, second_number, expected",
    [
        (6, 3, 2),
        (-6, 3, -2),
        (5, 2, 2.5),
        (0, 5, 0),
    ],
)
def test_division(first_number, second_number, expected):
    operation = Division()

    assert operation.execute(first_number, second_number) == expected


def test_division_by_zero():
    operation = Division()

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        operation.execute(10, 0)


def test_abstract_operation_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Operation()