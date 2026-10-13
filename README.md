# 🏦 Bank Management System

> **A Python-based, command-line banking application demonstrating Object-Oriented Programming (OOP), account management, and CSV file handling.**  
> Create accounts, deposit and withdraw money, check balances, and review transaction history through a simple interactive menu.

---

## 📌 Project Overview

The **Bank Management System** is a menu-driven Python project designed to simulate basic banking operations. It supports **Savings** and **Current** accounts, validates common transactions, maintains transaction records, and stores account information locally in CSV files so data can be loaded again when the program is restarted.

This project is intended for learning and demonstration. It is **not real banking software** and should not be used to store or manage real financial information.

## ✨ Key Features

- 🆕 **Create an Account** — Register an account holder and choose Savings or Current.
- 💰 **Deposit Money** — Add funds to an existing account.
- 💸 **Withdraw Money** — Withdraw funds while applying the account's minimum-balance rule.
- 📊 **Check Balance** — View account details and the current balance.
- 🧾 **Transaction History** — Review deposits, withdrawals, and opening deposits for an account.
- 🗃️ **CSV Data Persistence** — Save account details and transaction records locally.
- 🛡️ **Input Validation** — Check numeric input, account type, and transaction amounts.
- ⚠️ **Custom Error Handling** — Use a custom `BankError` exception for banking-related errors.
- 🧱 **OOP-Based Design** — Uses an abstract base class and specialized account classes.

## 🛠️ Technologies Used

- **Python 3.9+**
- `csv` — Read and write account and transaction records
- `abc` — Define the abstract `Account` base class
- `datetime` — Timestamp transactions

All imports used in the project are from Python's standard library. No third-party packages are required.

## 📁 Project Structure

```text
bank-management-system/
├── bank_management.py   # Python source code (rename to match your actual filename)
├── accounts.csv         # Account records, created when data is saved
├── transactions.csv     # Transaction history, created when data is saved
└── README.md            # Project documentation
```

> **Note:** `bank_management.py` is a suggested filename. If your script has a different name, use that name in the run command.

## ⚙️ Getting Started

### 1. Install Python

Install Python **3.9 or newer** from [python.org](https://www.python.org/downloads/).

Verify the installation:

```bash
python --version
```

Depending on your system, you may need:

```bash
python3 --version
```

### 2. Place the Project Files Together

Keep your Python script and `README.md` in the project folder. The program creates or updates `accounts.csv` and `transactions.csv` in its working directory.

### 3. Run the Application

If your Python file is named `bank_management.py`, run:

```bash
python bank_management.py
```

Replace the filename with your actual script name if it differs.

## 🚀 How to Use

After launching the program, the following menu appears:

```text
===== BANK ACCOUNT MANAGEMENT SYSTEM =====
1. Create account
2. Deposit money
3. Withdraw money
4. Check balance
5. Transaction history
6. Exit
```

Enter the number of the action you want to perform.

| Option | Action | Description |
|---|---|---|
| `1` | Create account | Enter the account holder's name, select an account type, and provide the opening deposit |
| `2` | Deposit money | Enter an account number and a positive deposit amount |
| `3` | Withdraw money | Enter an account number and a withdrawal amount that satisfies the account's balance rule |
| `4` | Check balance | Enter an account number to display account details and balance |
| `5` | Transaction history | Enter an account number to view its recorded transactions |
| `6` | Exit | Save data and close the application |

## 🏷️ Account Types & Balance Rules

The project defines two account types:

| Account type | Minimum balance required by this code | Opening deposit rule |
|---|---:|---|
| 🏦 Savings | 500 | Must be at least 500 |
| 💼 Current | 0 | Must be at least 0, though deposits must be positive for later deposit transactions |

The withdrawal method prevents a withdrawal that would reduce the account below its minimum balance. These values are rules implemented by this educational project, not statements about any real bank's policies.

## 💾 Data Storage

The application uses two local CSV files.

### `accounts.csv`

Stores account details using these columns:

```csv
acc_no,type,holder,balance
```

Each record contains an account number, account type, account holder's name, and current balance.

### `transactions.csv`

Stores transaction records using these columns:

```csv
acc_no,date,type,amount,balance_after
```

Each record includes the account number, transaction date and time, transaction type, amount, and resulting balance.

> 💡 Keep the CSV files in the program's working directory. They contain local project data and are not encrypted.

## 🧠 Python Concepts Demonstrated

| Concept | Application in this project |
|---|---|
| **Classes and Objects** | Models bank accounts and the bank manager |
| **Abstraction** | The `Account` abstract base class defines required methods |
| **Inheritance** | `SavingsAccount` and `CurrentAccount` extend `Account` |
| **Encapsulation** | Account number, holder, and balance are stored in private attributes |
| **Properties and Validation** | Getters and setters validate account-holder names and balances |
| **Polymorphism** | Account subclasses provide their own `account_type()` and `min_balance()` implementations |
| **Custom Exceptions** | `BankError` represents banking-operation errors |
| **File Handling** | CSV files persist account and transaction information |
| **Date and Time** | Transactions are timestamped using `datetime` |
| **Input Validation** | `read_number()` retries when numeric input is invalid |

## 🖥️ Example Interaction

The exact output depends on the actions you perform. A successful account creation may look like this:

```text
===== BANK ACCOUNT MANAGEMENT SYSTEM =====
1. Create account
2. Deposit money
3. Withdraw money
4. Check balance
5. Transaction history
6. Exit

Enter your choice (1-6): 1
Account holder name: Alex
Account type (1-Savings, 2-Current): 1
Opening deposit: 1000
Account created. Your account number is 1001.
```

*This is an illustrative example. Your account number and output may differ depending on existing saved data.*

## ⚠️ Important Notes & Limitations

- This is an educational command-line project, not a production banking system.
- CSV records are stored locally and are not encrypted or protected by user authentication.
- The code uses floating-point values for money; production financial systems generally require more careful monetary precision.
- The current implementation does not include transfers, interest calculation, account deletion, password protection, or a graphical interface.
- Keep backups of project CSV files if you need to preserve test records.

## 🔮 Future Enhancements

Ideas for a future version include:

- 🔐 Add login authentication and role-based access.
- 🔁 Support transfers between accounts.
- 📈 Add monthly statements and account summaries.
- 🏦 Add interest calculation for savings accounts.
- 🧪 Create automated unit tests for deposits, withdrawals, and validation.
- 🖥️ Build a graphical interface using Tkinter or a web framework.
- 🗄️ Replace CSV storage with SQLite or another database.
- 💱 Use `decimal.Decimal` for more reliable monetary calculations.

## 🎓 Learning Outcomes

This project provides practice with:

- Designing a menu-driven Python application.
- Applying OOP principles to a practical scenario.
- Validating inputs and handling exceptions.
- Reading and writing persistent data with CSV files.
- Recording transactions and maintaining account balances.
- Structuring code into reusable classes and methods.

## 👨‍💻 Author

**Your Name**  
*Python / Machine Learning Intern*

> Replace **Your Name** with your preferred name before publishing.

---

⭐ **If you find this project useful, consider starring the repository!**

Built with 🐍 Python and a passion for learning.
