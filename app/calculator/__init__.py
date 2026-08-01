"""Calculator service and calculation history."""

from app.calculation import Calculation, CalculationFactory


class Calculator:
    """Manage calculations and calculation history."""

    def __init__(self) -> None:
        """Initialize the calculator with empty history."""
        self._history: list[Calculation] = []

    @property
    def history(self) -> tuple[Calculation, ...]:
        """Return an immutable copy of the history."""
        return tuple(self._history)

    def calculate(
        self,
        operation_name: str,
        first_number: float,
        second_number: float,
    ) -> Calculation:
        """Create, perform, save, and return a calculation."""

        calculation = CalculationFactory.create(
            operation_name,
            first_number,
            second_number,
        )

        calculation.perform()
        self._history.append(calculation)

        return calculation

    def clear_history(self) -> None:
        """Remove all calculations from history."""
        self._history.clear()