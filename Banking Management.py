



"""**PROJECT 3 : BANK MANAGEMENT SYSTEM**"""

import csv
from abc import ABC, abstractmethod
from datetime import datetime

ACCOUNTS_FILE = "accounts.csv"
TRANSACTIONS_FILE = "transactions.csv"
TRANSACTION_FIELDS = ["acc_no", "date", "type", "amount", "balance_after"]


# ---------------------------------------------------------------- Exception
class BankError(Exception):
    """Raised when a banking action cannot be completed."""


# ------------------------------------------------- Abstract base class (abc)
class Account(ABC):
    """Base class for all bank accounts."""

    def __init__(self, acc_no, holder, balance=0):
        self.__acc_no = acc_no        # private attributes (encapsulation)
        self.__holder = ""
        self.__balance = 0
        self.holder = holder          # uses the setters below for validation
        self.balance = balance

    # Getters and setters
    @property
    def acc_no(self):
        return self.__acc_no

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, name):
        if not name.strip():
            raise ValueError("Account holder name cannot be empty.")
        self.__holder = name.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    # Common actions
    def deposit(self, amount):
        if amount <= 0:
            raise BankError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise BankError("Withdrawal amount must be greater than zero.")
        if self.balance - amount < self.min_balance():
            raise BankError(
                f"Insufficient balance (minimum balance: {self.min_balance()}).")
        self.balance -= amount

    def to_row(self):
        return [self.acc_no, self.account_type(), self.holder, f"{self.balance:.2f}"]

    def __str__(self):
        return (f"Account {self.acc_no} | {self.account_type()} | "
                f"{self.holder} | Balance: {self.balance:.2f}")

    # Every child class must implement these
    @abstractmethod
    def account_type(self):
        """Return the type name of the account."""

    @abstractmethod
    def min_balance(self):
        """Return the minimum balance that must be kept."""


# ------------------------------------------------ Derived classes (inheritance)
class SavingsAccount(Account):
    def account_type(self):
        return "Savings"

    def min_balance(self):
        return 500


class CurrentAccount(Account):
    def account_type(self):
        return "Current"

    def min_balance(self):
        return 0


ACCOUNT_TYPES = {"Savings": SavingsAccount, "Current": CurrentAccount}


# ---------------------------------------------------------------- Bank
class Bank:
    """Manages all accounts and saves them to CSV files."""

    def __init__(self):
        self.__accounts = {}
        self.__history = []
        self.load_data()

    # ----- file handling
    def load_data(self):
        try:
            with open(ACCOUNTS_FILE, newline="") as file:
                for row in csv.DictReader(file):
                    account_class = ACCOUNT_TYPES[row["type"]]
                    account = account_class(int(row["acc_no"]), row["holder"],
                                            float(row["balance"]))
                    self.__accounts[account.acc_no] = account
        except FileNotFoundError:
            print("No saved accounts found. Starting with an empty bank.")
        except (KeyError, ValueError):
            print("Some account records could not be read.")

        try:
            with open(TRANSACTIONS_FILE, newline="") as file:
                self.__history = list(csv.DictReader(file))
        except FileNotFoundError:
            pass

    def save_data(self):
        try:
            with open(ACCOUNTS_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["acc_no", "type", "holder", "balance"])
                for account in self.__accounts.values():
                    writer.writerow(account.to_row())

            with open(TRANSACTIONS_FILE, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=TRANSACTION_FIELDS)
                writer.writeheader()
                writer.writerows(self.__history)
        except OSError:
            print("Error: could not save data to file.")

    # ----- helper methods
    def __log(self, account, kind, amount):
        self.__history.append({
            "acc_no": account.acc_no,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "type": kind,
            "amount": f"{amount:.2f}",
            "balance_after": f"{account.balance:.2f}",
        })

    def get_account(self, acc_no):
        if acc_no not in self.__accounts:
            raise BankError("No account found with that number.")
        return self.__accounts[acc_no]

    # ----- banking actions
    def create_account(self, holder, acc_type, opening_amount):
        new_no = max(self.__accounts, default=1000) + 1
        account = ACCOUNT_TYPES[acc_type](new_no, holder)
        if opening_amount < account.min_balance():
            raise BankError(
                f"Opening deposit must be at least {account.min_balance()}.")
        account.balance = opening_amount
        self.__accounts[new_no] = account
        self.__log(account, "Opening Deposit", opening_amount)
        self.save_data()
        return account

    def deposit(self, acc_no, amount):
        account = self.get_account(acc_no)
        account.deposit(amount)
        self.__log(account, "Deposit", amount)
        self.save_data()
        return account

    def withdraw(self, acc_no, amount):
        account = self.get_account(acc_no)
        account.withdraw(amount)
        self.__log(account, "Withdraw", amount)
        self.save_data()
        return account

    def get_history(self, acc_no):
        self.get_account(acc_no)  # raises an error if the account does not exist
        return [t for t in self.__history if str(t["acc_no"]) == str(acc_no)]


# ---------------------------------------------------------------- Menu
def read_number(message, number_type=int):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return number_type(input(message))
        except ValueError:
            print("Please enter a valid number.")


def main():
    bank = Bank()

    menu = """
===== BANK ACCOUNT MANAGEMENT SYSTEM =====
1. Create account
2. Deposit money
3. Withdraw money
4. Check balance
5. Transaction history
6. Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                holder = input("Account holder name: ")
                kind = input("Account type (1-Savings, 2-Current): ").strip()
                if kind not in ("1", "2"):
                    raise BankError("Invalid account type.")
                acc_type = "Savings" if kind == "1" else "Current"
                opening = read_number("Opening deposit: ", float)
                account = bank.create_account(holder, acc_type, opening)
                print(f"Account created. Your account number is {account.acc_no}.")

            elif choice == "2":
                acc_no = read_number("Account number: ")
                amount = read_number("Amount to deposit: ", float)
                account = bank.deposit(acc_no, amount)
                print(f"Deposit successful. New balance: {account.balance:.2f}")

            elif choice == "3":
                acc_no = read_number("Account number: ")
                amount = read_number("Amount to withdraw: ", float)
                account = bank.withdraw(acc_no, amount)
                print(f"Withdrawal successful. New balance: {account.balance:.2f}")

            elif choice == "4":
                print(bank.get_account(read_number("Account number: ")))

            elif choice == "5":
                history = bank.get_history(read_number("Account number: "))
                if not history:
                    print("No transactions found.")
                for t in history:
                    print(f"{t['date']} | {t['type']:<15} | "
                          f"Amount: {t['amount']:>10} | "
                          f"Balance: {t['balance_after']:>10}")

            elif choice == "6":
                bank.save_data()
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-6.")

        except (BankError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()