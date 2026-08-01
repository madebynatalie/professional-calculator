"""Calculation classes and calculation factory."""

from dataclasses import dataclass

from app.operation import (
    Addition,
    Division,
    Multiplication,
    Operation,
    Subtraction,
)


@dataclass
class Calculation:
    """Represent a calculation with two numbers and one operation."""

    first_number: float
    second_number: float
    operation: Operation
    operation_symbol: str

    def perform(self) -> float:
        """Perform and return the calculation result."""
        return self.operation.execute(
            self.first_number,
            self.second_number,
        )

    def __str__(self) -> str:
        """Return a readable version of the calculation."""
        result = self.perform()

        return (
            f"{self.first_number:g} {self.operation_symbol} "
            f"{self.second_number:g} = {result:g}"
        )


class CalculationFactory:
    """Create calculations based on an operation name."""

    _operations = {
        "add": ("+", Addition),
        "subtract": ("-", Subtraction),
        "multiply": ("*", Multiplication),
        "divide": ("/", Division),
    }

    @classmethod
    def create(
        cls,
        operation_name: str,
        first_number: float,
        second_number: float,
    ) -> Calculation:
        """Create and return a calculation."""

        normalized_name = operation_name.strip().lower()

        if normalized_name not in cls._operations:
            raise ValueError(
                f"Unsupported operation: {operation_name}"
            )

        symbol, operation_class = cls._operations[normalized_name]

        return Calculation(
            first_number=first_number,
            second_number=second_number,
            operation=operation_class(),
            operation_symbol=symbol,
        )