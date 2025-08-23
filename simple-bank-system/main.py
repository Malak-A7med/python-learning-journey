class User:
    def __init__(self, acc_id, n, a, g, b):
        self.acc_id = acc_id
        self.name = n
        self.age = a
        self.gender = g
        self.balance = b

    def show(self):
        print("User Data:")
        print("-" * 20)
        print(f"Account ID: {self.acc_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Balance: {self.balance}")
        print("-" * 20)


class Bank:
    def __init__(self):
        self.users = {}  

    def create_account(self, n, a, g, b):
        acc_id = len(self.users) + 1   
        self.users[acc_id] = User(acc_id, n, a, g, b)
        print(f"Account created successfully! Your Account ID is {acc_id}")

    def get_user(self, acc_id):
        return self.users.get(acc_id, None)


# ---------------- Main Program ----------------
CIB = Bank()

while True:
    print("\n==== Welcome to our Bank ====")
    print("1. Create Account")
    print("2. Show User Data")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. View Balance")
    print("6. Exit\n")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        balance = float(input("Enter Initial Balance: "))
        CIB.create_account(name, age, gender, balance)

    elif choice in ["2", "3", "4", "5"]:
        acc_id = int(input("Enter Account ID: "))
        user = CIB.get_user(acc_id)
        if not user:
            print("Account not found!")
            continue

        if choice == "2":
            user.show()
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            user.balance += amount
            print(f"{amount} added, New Balance = {user.balance}")
        elif choice == "4":
            amount = float(input("Enter amount to withdraw: "))
            if user.balance >= amount:
                user.balance -= amount
                print(f"{amount} withdrawn, New Balance = {user.balance}")
            else:
                print("Insufficient balance!")
        elif choice == "5":
            print(f"Your current balance is: {user.balance}")

    elif choice == "6":
        print("Thank you for using our Bank")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
