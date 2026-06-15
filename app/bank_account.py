class BankAccount:
    def __init__(self,account_number,owner_name,intial_balance):
        self.account_number = account_number
        self.owner_name = owner_name

        self._balance = None

        self.balance = intial_balance

    @property
    def balance(self):
        return self._balance


    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Catastrophic State Blocked: Account balance cannot be negative.")
         
        self._balance = value
        print("Added sucessfully")

    
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        self.balance +=amount
        print(f"Sucessfully debited")

    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount >self.balance:
            raise ValueError("Not enough balance")

        self.balance -=amount
        print("Withdraw Sucessful")

    def get_balance(self):
        return self.balance

    def display_info(self) -> None:
        print(f"Account: {self.account_number} | Owner: {self.owner_name} | Balance: ${self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self,account_number,owner_name,initial_balance,interest_rate):
        super().__init__(account_number,owner_name,initial_balance)

        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate

        if interest_earned > 0:
            self.deposit(interest_earned)
            print("Interest added to balance")
        else:
            print("No interest applied (balance is zero).")


class CheckingAccount(BankAccount):
    def __init__(self,account_number,owner_name,initial_balance,overdraft_limit):
        super().__init__(account_number,owner_name,initial_balance)

        self.overdraft_limit = overdraft_limit


    def withdraw(self,amount):
        predicted_balance = self.balance - amount

        if predicted_balance < -self.overdraft_limit:
            raise ValueError("Transaction declined: amount is over the value")

        self._balance = predicted_balance
        print("Withdraw sucessful") 
        self.display_info()