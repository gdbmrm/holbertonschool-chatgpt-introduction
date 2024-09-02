#!/usr/bin/python3

class Checkbook:
    """
    The Checkbook class simulates a bank account with deposit, withdrawal, and balance checking operations.
    """
    def __init__(self):
        """
        Initializes a new Checkbook object with an initial balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the account balance and prints the transaction details.

        Args:
            amount (float): The amount to deposit into the account.

        Returns:
            None. Prints the deposited amount and the current balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account balance if sufficient funds are available;
        otherwise, prints an insufficient funds message.

        Args:
            amount (float): The amount to withdraw from the account.

        Returns:
            None. Prints the withdrawn amount and the current balance, or an error message if funds are insufficient.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current account balance.

        Args:
            None.

        Returns:
            None. Prints the current balance of the account.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    The main function allows the user to interact with the bank account via command-line input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Deposit amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Withdrawal amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    """
    Checks if the script is run directly (not imported as a module) and calls the main function to start the application.
    """
    main()