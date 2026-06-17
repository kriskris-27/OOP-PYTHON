from app.bank_account import BankAccount, CheckingAccount, SavingsAccount, process_account_transactions


# kris_acc = BankAccount("IOB-123","Kris",10)

# savings = SavingsAccount("SAV-2026", "Krishnakumar", 50000.0, 0.05)

# checking = CheckingAccount("CHE-123","Kris",1000,3000)
# checking.withdraw(3000)
# checking.withdraw(4000)

basic_acc = BankAccount("BAS-101", "Rohan", 1000.0)
savings_acc = SavingsAccount("SAV-202", "Anjali", 5000.0, interest_rate=0.05)
checking_acc = CheckingAccount("CHK-303", "Krishnakumar", 2000.0, overdraft_limit=3000.0)

bankaccounts = [basic_acc,savings_acc,checking_acc]

process_account_transactions(bankaccounts,"withdraw",1000)