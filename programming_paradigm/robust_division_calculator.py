def safe_divide(numerator, denominator):
    """Perform division with error handling."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division
        return num / denom
    
    except ZeroDivisionError:
        # Ensure the exact error message is returned
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter valid numeric values."

# Example usage
if __name__ == "__main__":
    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")
    
    result = safe_divide(numerator, denominator)
    print(result)
