# Professional Command-Line Calculator

A modular command-line calculator written in Python that demonstrates object-oriented programming, testing, and continuous integration.

## Features

- Addition, subtraction, multiplication, and division
- Interactive REPL interface
- Calculation history
- Help, history, clear, and exit commands
- Input validation and error handling
- LBYL and EAFP error handling
- Factory design pattern
- Unit and parameterized tests
- 100% test coverage
- GitHub Actions CI

## Project Structure

```text
app/
├── calculator/
├── calculation/
├── operation/
└── __main__.py

tests/
├── test_calculator.py
├── test_calculations.py
└── test_operations.py
```

## Installation

```bash
git clone https://github.com/madebynatalie/professional-calculator.git
cd professional-calculator

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Running the Calculator

```bash
python -m app
```

## Running Tests

```bash
pytest
```

## Error Handling

This project demonstrates both:

- **LBYL (Look Before You Leap):** checks conditions before performing operations.
- **EAFP (Easier to Ask Forgiveness than Permission):** uses `try/except` blocks to handle invalid input and runtime errors.
