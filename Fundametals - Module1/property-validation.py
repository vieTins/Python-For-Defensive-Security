# Create Account(balance) where balance never drops below 0; deposit/withdraw methods must use the property.
class Account:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = float(value)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw must be positive.")
        self.balance -= amount

    def __repr__(self) -> str:
        return f"Account(balance={self.balance})"

# Example usage:
account1 = Account()
account1.deposit(100)
account1.withdraw(50)
print(account1)