"""Tests for the calculator service."""

import pytest

from app.calculator import Calculator


def test_calculator_starts_with_empty_history():
    calculator = Calculator()

    assert calculator.history == ()


def test_calculator_performs_calculation():
    calculator = Calculator()

    calculation = calculator.calculate("add", 2, 3)

    assert calculation.perform() == 5


def test_calculator_adds_successful_calculation_to_history():
    calculator = Calculator()

    calculation = calculator.calculate("multiply", 4, 5)

    assert calculator.history == (calculation,)


def test_calculator_maintains_multiple_history_items():
    calculator = Calculator()

    first = calculator.calculate("add", 2, 3)
    second = calculator.calculate("subtract", 10, 4)

    assert calculator.history == (first, second)


def test_calculator_does_not_save_failed_calculation():
    calculator = Calculator()

    with pytest.raises(ZeroDivisionError):
        calculator.calculate("divide", 10, 0)

    assert calculator.history == ()


def test_calculator_clears_history():
    calculator = Calculator()
    calculator.calculate("add", 2, 3)

    calculator.clear_history()

    assert calculator.history == ()


def test_history_is_returned_as_tuple():
    calculator = Calculator()
    calculator.calculate("add", 2, 3)

    assert isinstance(calculator.history, tuple)