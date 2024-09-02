#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un nombre entier non négatif.

    Le factoriel d'un nombre entier n (noté n!) est le produit de tous les entiers
    positifs inférieurs ou égaux à n. Par définition, 0! est égal à 1.

    Args:
        n (int): Un entier non négatif dont le factoriel est à calculer.

    Returns:
        int: Le factoriel du nombre n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Récupère l'argument de ligne de commande et le convertit en entier
f = factorial(int(sys.argv[1]))

# Affiche le résultat du calcul du factoriel
print(f)