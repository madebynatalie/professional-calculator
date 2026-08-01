"""Arithmetic operation classes."""

from abc import ABC, abstractmethod


class Operation(ABC):
    """Abstract base class for arithmetic operations."""

    @abstractmethod
    def execute(self, first_number: float, second_number: float) -> float:
        """Perform an arithmetic operation."""
        raise NotImplementedError


class Addition(Operation):
    """Perform addition."""

    def execute(self, first_number: float, second_number: float) -> float:
        return first_number + second_number


class Subtraction(Operation):
    """Perform subtraction."""

    def execute(self, first_number: float, second_number: float) -> float:
        return first_number - second_number


class Multiplication(Operation):
    """Perform multiplication."""

    def execute(self, first_number: float, second_number: float) -> float:
        return first_number * second_number


class Division(Operation):
    """Perform division."""

    def execute(self, first_number: float, second_number: float) -> float:
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return first_number / second_number