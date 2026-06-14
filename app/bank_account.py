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





