class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default: 0)."""
        self._account_balance = initial_balance  # Store the initial balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:  # Ensure only positive amounts are deposited
            self._account_balance += amount  # Update the balance

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds are available."""
        if amount <= self._account_balance:  # Check if there are sufficient funds
            self._account_balance -= amount  # Deduct the amount
            return True  # Indicate success
        return False  # Indicate failure due to insufficient funds

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")  # Print balance formatted as currency
