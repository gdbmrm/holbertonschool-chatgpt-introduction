#!/usr/bin/python3

import sys

class Checkbook:
    """
    La classe Checkbook simule un compte bancaire avec des opérations de dépôt, de retrait et de consultation du solde.
    """
    def __init__(self):
        """
        Initialise un nouvel objet Checkbook avec un solde initial de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Ajoute un montant spécifié au solde du compte et affiche les détails de la transaction.

        Args:
            amount (float): Le montant à déposer dans le compte.

        Returns:
            None. Affiche le montant déposé et le solde actuel.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant spécifié du solde du compte si le solde est suffisant; sinon, affiche un message d'insuffisance de fonds.

        Args:
            amount (float): Le montant à retirer du compte.

        Returns:
            None. Affiche le montant retiré et le solde actuel, ou un message d'erreur si les fonds sont insuffisants.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.

        Args:
            None.

        Returns:
            None. Affiche le solde actuel du compte.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Fonction principale qui permet à l'utilisateur d'interagir avec le compte bancaire via des commandes en ligne de commande.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    """
    Vérifie si le script est exécuté directement (et non importé comme module) et appelle la fonction main() pour démarrer l'application.
    """
    main()