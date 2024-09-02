#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu avec des séparateurs pour les lignes et les colonnes.
    
    Args:
        board (list of list of str): Le plateau de jeu Tic-Tac-Toe.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.

    Args:
        board (list of list of str): Le plateau de jeu Tic-Tac-Toe.

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
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while not check_winner(board) and moves < 9:
        print_board(board)
        
        # Validation des entrées
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input. Please enter 0, 1, or 2.")
                    continue
                
                if board[row][col] == " ":
                    break
                else:
                    print("That spot is already taken! Try again.")
            
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        # Effectuer le coup
        board[row][col] = player
        moves += 1
        
        # Changer de joueur
        player = "O" if player == "X" else "X"

    print_board(board)
    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()