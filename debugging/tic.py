#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu.
    
    Args:
        board (list of list of str): Le plateau de jeu sous forme de liste 2D.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie s'il y a un gagnant.

    Args:
        board (list of list of str): Le plateau de jeu.

    Returns:
        bool: True si un joueur a gagné, sinon False.
    """
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Fonction principale pour jouer au Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Validation des entrées
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input. Please enter 0, 1, or 2.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Mettre à jour le plateau de jeu
        board[row][col] = player
        
        # Vérification du gagnant
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Changement de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
