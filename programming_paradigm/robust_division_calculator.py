def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        # Convert inputs to float for division
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division and return the result
        return num / denom
    
    except ZeroDivisionError:
        # Exact error message for division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Exact error message for non-numeric input
        return "Error: Please enter numeric values only."  # Ensure this matches the expected message

# Example usage
if __name__ == "__main__":
    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")
    
    result = safe_divide(numerator, denominator)
    print(result)
