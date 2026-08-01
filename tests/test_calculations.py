"""Tests for calculations and the calculation factory."""

import pytest

from app.calculation import Calculation, CalculationFactory
from app.operation import Addition, Division, Multiplication, Subtraction


@pytest.mark.parametrize(
    "operation, first_number, second_number, expected",
    [
        (Addition(), 2, 3, 5),
        (Subtraction(), 5, 3, 2),
        (Multiplication(), 4, 3, 12),
        (Division(), 10, 2, 5),
    ],
)
def test_calculation_perform(
    operation,
    first_number,
    second_number,
    expected,
):
    calculation = Calculation(
        first_number=first_number,
        second_number=second_number,
        operation=operation,
        operation_symbol="?",
    )

    assert calculation.perform() == expected


@pytest.mark.parametrize(
    "operation_name, first_number, second_number, expected",
    [
        ("add", 2, 3, 5),
        ("ADD", 2, 3, 5),
        (" subtract ", 10, 4, 6),
        ("multiply", 4, 5, 20),
        ("divide", 10, 2, 5),
    ],
)
def test_factory_creates_correct_calculation(
    operation_name,
    first_number,
    second_number,
    expected,
):
    calculation = CalculationFactory.create(
        operation_name,
        first_number,
        second_number,
    )

    assert calculation.perform() == expected


def test_factory_rejects_unsupported_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        CalculationFactory.create("power", 2, 3)


def test_calculation_string():
    calculation = CalculationFactory.create("add", 2, 3)

    assert str(calculation) == "2 + 3 = 5"


def test_calculation_string_with_decimal():
    calculation = CalculationFactory.create("divide", 5, 2)

    assert str(calculation) == "5 / 2 = 2.5"


def test_calculation_division_by_zero():
    calculation = CalculationFactory.create("divide", 10, 0)

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculation.perform()