"""3. Encapsulation
Encapsulation hides the internal state and provides controlled access through methods.

Example:"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Deposit amount must be positive."

    def get_balance(self):  # Public method to access private balance
        return self.__balance

# Create account
account = BankAccount("12345", 1000)

print(account.deposit(500))  # Output: Deposited 500. New balance: 1500
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # Error: Cannot access private variable directly
