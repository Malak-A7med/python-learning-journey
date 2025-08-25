# 🏦 Simple Bank Management System in Python

A basic command-line banking application in Python. It allows users to create accounts, deposit and withdraw money, display user data, and check their balance.

## Features

- **Create Account**: Register a new user with name, age, gender, and initial balance. Each user gets a unique Account ID.
- **Show User Data**: Display all information of a specific user using their Account ID.
- **Deposit**: Add money to a user's balance.
- **Withdraw**: Remove money from a user's balance (if sufficient funds are available).
- **View Balance**: Check current balance for any account.
- **Exit**: End the program with a thank you message.

## How to Run

1. Make sure you have Python 3 installed.
2. Copy the code to a file called `bank.py`.
3. Open your terminal and run:
   ```bash
   python bank.py
   ```
4. Follow the on-screen instructions and enter the number of your chosen option.

## Example Usage

```
==== Welcome to our Bank ====
1. Create Account
2. Show User Data
3. Deposit
4. Withdraw
5. View Balance
6. Exit

Enter your choice (1-6): 
```

- When creating an account, you will be prompted for your name, age, gender, and initial deposit.
- For other operations, you need to enter your Account ID.

## Notes

- Account IDs start from 1 and increment for each new user.
- All user information and balances are stored in memory for the current session only (data will not be saved when you exit).
- The code is easy to extend and customize for more banking features.

---

This project is great for learning about classes, objects, and basic data handling in Python.
