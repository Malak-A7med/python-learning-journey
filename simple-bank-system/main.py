class User:
    def __init__(self, n, a, g, b):
        self.name = n
        self.age = a
        self.gender = g
        self.balance = b

    def show(self):
        print("User Data:")
        print("-" * 20)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Balance: {self.balance}")
        print("-" * 20)


class Bank(User):
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} added, New Balance is = {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn, New Balance is = {self.balance}")
        else:
            print("Insufficient balance!")
   
    def view_balance(self):
        print(f"Your current balance is: {self.balance}")


CIB = Bank("Malak", 20, "female", 20000)
while True:
    print(f"\n==== Welcome {CIB.name} to our Bank ====")
    print("1. Show user data")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View balance")
    print("5. Exit\n")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        CIB.show()
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        CIB.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        CIB.withdraw(amount)
    elif choice == "4":
        CIB.view_balance()
    elif choice == "5":
        print("Thank you for using our Bank ❤️")
        break
    else:
        print("Invalid choice. Please enter a numbe r from 1 to 5.")

