# Task 10: Object-Oriented Programming (OOP)
# Python Developer Internship

class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance   # encapsulation (private)

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount!")

    # Display balance
    def display_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    # Getter (encapsulation)
    def get_balance(self):
        return self.__balance


# Inheritance + Polymorphism
class SavingsAccount(BankAccount):
    def __init__(self, name, acc_no, balance=0, interest_rate=0.04):
        super().__init__(name, acc_no, balance)
        self.interest_rate = interest_rate

    # Overriding method
    def display_balance(self):
        balance = self.get_balance()
        interest = balance * self.interest_rate
        print(f"Balance: ₹{balance}")
        print(f"Interest (yearly): ₹{interest}")


# ----------- Main Program -----------
if __name__ == "__main__":
    print("🏦 Welcome to Python Bank System")

    name = input("Enter account holder name: ")
    acc = input("Enter account number: ")

    account = SavingsAccount(name, acc, 0)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)

        elif choice == "3":
            account.display_balance()

        elif choice == "4":
            print("Thank you for using Python Bank 💙")
            break

        else:
            print("Invalid choice!")
