from app.bank_account import BankAccount, CheckingAccount, SavingsAccount


# kris_acc = BankAccount("IOB-123","Kris",10)

# savings = SavingsAccount("SAV-2026", "Krishnakumar", 50000.0, 0.05)

checking = CheckingAccount("CHE-123","Kris",1000,3000)
checking.withdraw(3000)
# checking.withdraw(4000)
