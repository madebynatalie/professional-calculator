"""Tests for the calculator service and command-line interface."""

from unittest.mock import patch

import pytest

from app.__main__ import (
    HELP_MESSAGE,
    display_history,
    get_number,
    process_operation,
    run_calculator,
)
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

    def test_get_number_accepts_valid_input():
      with patch("builtins.input", return_value="4.5"):
        assert get_number("Number: ") == 4.5


def test_get_number_retries_after_invalid_input(capsys):
    with patch("builtins.input", side_effect=["hello", "5"]):
        result = get_number("Number: ")

    captured = capsys.readouterr()

    assert result == 5
    assert "Invalid number" in captured.out


def test_display_empty_history(capsys):
    calculator = Calculator()

    display_history(calculator)

    captured = capsys.readouterr()

    assert "No calculations have been performed" in captured.out


def test_display_history_with_calculation(capsys):
    calculator = Calculator()
    calculator.calculate("add", 2, 3)

    display_history(calculator)

    captured = capsys.readouterr()

    assert "Calculation history:" in captured.out
    assert "1. 2 + 3 = 5" in captured.out


def test_process_operation_success(capsys):
    calculator = Calculator()

    with patch("app.__main__.get_number", side_effect=[5, 3]):
        process_operation(calculator, "subtract")

    captured = capsys.readouterr()

    assert "Result: 5 - 3 = 2" in captured.out


def test_process_operation_division_by_zero(capsys):
    calculator = Calculator()

    with patch("app.__main__.get_number", side_effect=[5, 0]):
        process_operation(calculator, "divide")

    captured = capsys.readouterr()

    assert "Error: Cannot divide by zero" in captured.out


def test_process_operation_invalid_operation(capsys):
    calculator = Calculator()

    with patch("app.__main__.get_number", side_effect=[5, 2]):
        process_operation(calculator, "power")

    captured = capsys.readouterr()

    assert "Unsupported operation" in captured.out


def test_run_calculator_help_and_exit(capsys):
    with patch("builtins.input", side_effect=["help", "exit"]):
        run_calculator()

    captured = capsys.readouterr()

    assert HELP_MESSAGE in captured.out
    assert "Thank you for using the calculator" in captured.out


def test_run_calculator_invalid_command_and_exit(capsys):
    with patch("builtins.input", side_effect=["wrong", "exit"]):
        run_calculator()

    captured = capsys.readouterr()

    assert "Invalid command" in captured.out


def test_run_calculator_history_and_exit(capsys):
    with patch("builtins.input", side_effect=["history", "exit"]):
        run_calculator()

    captured = capsys.readouterr()

    assert "No calculations have been performed" in captured.out


def test_run_calculator_clear_and_exit(capsys):
    with patch("builtins.input", side_effect=["clear", "exit"]):
        run_calculator()

    captured = capsys.readouterr()

    assert "Calculation history cleared" in captured.out


def test_run_calculator_operation_and_exit(capsys):
    with patch(
        "builtins.input",
        side_effect=["add", "2", "3", "exit"],
    ):
        run_calculator()

    captured = capsys.readouterr()

    assert "Result: 2 + 3 = 5" in captured.out