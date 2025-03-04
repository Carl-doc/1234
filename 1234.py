class Bank:
    def __init__(self, owner, account_number):
        self.owner = owner
        self._account_number = account_number


class AccountNumber(Bank):
    def get_account_number(self):
        return self._account_number
    

class ATM:
    def __init__(self):
        self.__balance = 1000  # Initialize balance to 1000

    def check_balance(self):
        return f"Balance: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. {self.check_balance()}"
        return "Amount must be positive."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. {self.check_balance()}"
        return "Insufficient funds or invalid amount."


# Example usage
bank_account = Bank("jumploks", 6969)
atm_machine = ATM()

print(atm_machine.check_balance())  # Display initial balance
print(atm_machine.deposit(69))       # Deposit money
print(atm_machine.withdraw(50))      # Withdraw money
print(atm_machine.check_balance())    # Display balance after transactions