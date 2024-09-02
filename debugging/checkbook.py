#!/usr/bin/python3
"""
Checkbook Simulation

Ce script permet de simuler un registre de chèques simple où vous pouvez déposer de l'argent, retirer de l'argent et consulter votre solde actuel.
"""

class Checkbook:
    """
    Une classe pour représenter un registre de chèques.

    Attributs :
    ----------
    balance : float
        Le solde actuel du registre.

    Méthodes :
    ---------
    deposit(amount):
        Ajoute un montant au solde actuel.
    
    withdraw(amount):
        Soustrait un montant du solde actuel s'il y a suffisamment de fonds.
    
    get_balance():
        Affiche le solde actuel.
    """

    def __init__(self):
        """
        Initialise un nouveau registre de chèques avec un solde de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Ajoute un montant au solde actuel.

        Paramètres :
        -----------
        amount : float
            Le montant à déposer.

        Retour :
        -------
        None
        """
        if amount <= 0:
            print("Veuillez entrer un montant positif à déposer.")
            return
        self.balance += amount
        print("Déposé : ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Soustrait un montant du solde actuel s'il y a suffisamment de fonds.

        Paramètres :
        -----------
        amount : float
            Le montant à retirer.

        Retour :
        -------
        None
        """
        if amount <= 0:
            print("Veuillez entrer un montant positif à retirer.")
            return
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retiré : ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel.

        Retour :
        -------
        None
        """
        print("Solde actuel : ${:.2f}".format(self.balance))

def main():
    """
    Point d'entrée principal pour l'exécution du script.

    Permet à l'utilisateur de choisir entre déposer de l'argent, retirer de l'argent, consulter le solde ou quitter l'application.

    Retour :
    -------
    None
    """
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (deposit, withdraw, balance, exit) : ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Entrez le montant à déposer : $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Entrez le montant à retirer : $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
