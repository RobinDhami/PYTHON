class BankAccount:
    total_accounts = 0

    def __init__(self, account_nmr, balance):
        self.account_nmr = account_nmr
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

# Creating instances of BankAccount
a1 = BankAccount("876545678", 10000)
a2 = BankAccount("45675454", 20089)

# Testing deposit and withdraw methods
a1.deposit(500)  # Deposit 500 into a1
a1.withdraw(200)  # Withdraw 200 from a1

print(f"Account 1 Balance: {a1.get_balance()}")  # Output: 10200
print(f"Account 2 Balance: {a2.get_balance()}")  # Output: 20089

# Printing the total number of accounts
print(f"Total Accounts: {BankAccount.get_total_accounts()}")  # Output: 2

# Testing invalid operations
try:
    a1.withdraw(20000)  # This should raise an error
except ValueError as e:
    print(e)  # Output: Insufficient funds
