"""Command-line interface for the calculator application."""

from app.calculator import Calculator


HELP_MESSAGE = """
Available operations:
  add        Add two numbers
  subtract   Subtract the second number from the first
  multiply   Multiply two numbers
  divide     Divide the first number by the second

Special commands:
  help       Display these instructions
  history    Display calculation history
  clear      Clear calculation history
  exit       Exit the calculator
""".strip()


def get_number(prompt: str) -> float:
    """Prompt the user until a valid number is entered."""

    while True:
        user_input = input(prompt).strip()

        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def display_history(calculator: Calculator) -> None:
    """Display calculations completed during the session."""

    if not calculator.history:
        print("No calculations have been performed.")
        return

    print("Calculation history:")

    for index, calculation in enumerate(calculator.history, start=1):
        print(f"{index}. {calculation}")


def process_operation(
    calculator: Calculator,
    command: str,
) -> None:
    """Request numbers and perform an arithmetic operation."""

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    try:
        calculation = calculator.calculate(
            command,
            first_number,
            second_number,
        )
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Result: {calculation}")


def run_calculator() -> None:
    """Run the calculator REPL."""

    calculator = Calculator()
    valid_operations = {"add", "subtract", "multiply", "divide"}

    print("Professional Command-Line Calculator")
    print("Type 'help' for instructions or 'exit' to quit.")

    while True:
        command = input("\nEnter an operation or command: ").strip().lower()

        if command == "exit":
            print("Thank you for using the calculator.")
            break

        if command == "help":
            print(HELP_MESSAGE)
            continue

        if command == "history":
            display_history(calculator)
            continue

        if command == "clear":
            calculator.clear_history()
            print("Calculation history cleared.")
            continue

        if command not in valid_operations:
            print("Invalid command. Type 'help' to see available commands.")
            continue

        process_operation(calculator, command)


if __name__ == "__main__":  # pragma: no cover
    run_calculator()