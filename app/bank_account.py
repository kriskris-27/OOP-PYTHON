class BankAccount:
    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        # Protected attributes initialized with underscores
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = initial_balance

    # --- Properties (Getters/Setters) for Raw Data ---
    @property
    def account_number(self) -> str:
        """Read-only property for account number."""
        return self._account_number

    @property
    def owner_name(self) -> str:
        """Getter for owner name."""
        return self._owner_name

    @owner_name.setter
    def owner_name(self, new_name: str):
        """Setter for owner name with a validation guard."""
        if not new_name.strip():
            raise ValueError("Owner name cannot be empty.")
        self._owner_name = new_name

    @property
    def balance(self) -> float:
        """Getter for balance (acts as get_balance())."""
        return self._balance

    # --- Instance Methods for Actions / Operations ---
    def deposit(self, amount: float) -> None:
        """Executes the action of depositing money."""
        if amount <= 0:
            print("Deposit rejected: Amount must be positive.")
            return
        self._balance += amount
        print(f"[{self.account_number}] Deposited ${amount:.2f}. New Balance: ${self._balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        """Executes the action of withdrawing money with basic validation."""
        if amount <= 0:
            print("Withdrawal rejected: Amount must be positive.")
            return False
        
        if amount > self._balance:
            print(f"[{self.account_number}] Withdrawal rejected: Insufficient funds.")
            return False
            
        self._balance -= amount
        print(f"[{self.account_number}] Withdrew ${amount:.2f}. New Balance: ${self._balance:.2f}")
        return True

    def display_info(self) -> None:
        """Helper to print basic account specifications."""
        print(f"Account: {self.account_number} | Owner: {self.owner_name} | Balance: ${self.balance:.2f}")


# --- Inheritance: Child Classes ---

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, owner_name: str, initial_balance: float, interest_rate: float):
        # Pass core data up to parent delivery boxes
        super().__init__(account_number, owner_name, initial_balance)
        self._interest_rate = interest_rate  # e.g., 0.05 for 5%

    def apply_interest(self) -> None:
        """Calculates interest on current balance and adds it via deposit."""
        interest_earned = self._balance * self._interest_rate
        print(f"Applying interest rate of {self._interest_rate * 100}%...")
        self.deposit(interest_earned)


class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, owner_name: str, initial_balance: float, overdraft_limit: float):
        super().__init__(account_number, owner_name, initial_balance)
        self._overdraft_limit = overdraft_limit  # Maximum negative amount allowed

    # Polymorphism: Overriding the parent's withdraw() method behavior
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal rejected: Amount must be positive.")
            return False

        # Custom validation check that includes overdraft limit allowance
        if amount > (self._balance + self._overdraft_limit):
            print(f"[{self.account_number}] Withdrawal rejected: Exceeds overdraft limit.")
            return False

        self._balance -= amount
        print(f"[{self.account_number}] Overdraft-Approved Withdrawal: ${amount:.2f}. New Balance: ${self._balance:.2f}")
        return True


# --- Demonstration of Polymorphism and Workflows ---
if __name__ == "__main__":
    print("--- Creating Accounts ---")
    # Initializing account types
    savings = SavingsAccount("SAV-101", "Alice Smith", 1000.0, 0.05)
    checking = CheckingAccount("CHK-202", "Bob Jones", 200.0, 500.0)

    # Put both unique objects into a single standardized collection
    accounts_list = [savings, checking]

    print("\n--- Processing Accounts Polymorphically ---")
    # Even though they are different types, we can treat them identically 
    # and call the exact same methods on them safely.
    for account in accounts_list:
        account.display_info()
        account.deposit(50.0)
        print("-" * 40)

    print("\n--- Specific Account Behaviors ---")
    # 1. Action behavior specific to Savings Account
    savings.apply_interest()
    
    print()
    
    # 2. Polymorphic overridden method behavior specific to Checking Account
    checking.display_info()
    checking.withdraw(400.0)  # Goes into negative balance, but allowed by overdraft
    checking.withdraw(400.0)  # Rejected! Exceeds the $500 limit.