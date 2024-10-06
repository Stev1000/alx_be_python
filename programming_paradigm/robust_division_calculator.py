# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        return num / denom  # Return the result if no exceptions occur
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input. Please provide numbers."
