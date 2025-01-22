import sys

class BankAccount:
    def __init__(self,initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self,amount):

        if amount > 0:

            self.account_balance += amount
            return self.account_balance
        return None

    def withdraw(self,amount):
        if 0 < amount <=self.account_balance:
            self.account_balance -= amount
            return True
        return False
    def display_balance (self):
        print(f"Current Balance: ${self.account_balance:.2f}")


if __name__ == "__main__":
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:

        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    elif command == "display":

        account.display_balance()