# test_tic_tac_toe.py

import unittest
from unittest.mock import patch
from io import StringIO
from tic import print_board, check_winner, tic_tac_toe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Initialisation du plateau de jeu
        self.board = [[" "] * 3 for _ in range(3)]

    def test_check_winner_row(self):
        # Test de la détection de victoire sur une ligne
        self.board[0] = ["X", "X", "X"]
        self.assertTrue(check_winner(self.board))

    def test_check_winner_column(self):
        # Test de la détection de victoire sur une colonne
        self.board[0][0] = self.board[1][0] = self.board[2][0] = "O"
        self.assertTrue(check_winner(self.board))

    def test_check_winner_diagonal(self):
        # Test de la détection de victoire sur une diagonale
        self.board[0][0] = self.board[1][1] = self.board[2][2] = "X"
        self.assertTrue(check_winner(self.board))

    @patch('builtins.input', side_effect=['a', '5', '-1'])
    def test_invalid_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                tic_tac_toe()
            output = fake_out.getvalue()
            self.assertIn("Invalid input. Please enter numbers only.", output)
            self.assertIn("Coordinates out of bounds. Try again.", output)


    @patch('builtins.input', side_effect=['1', '1', '1', '2', '2', '2'])
    def test_spot_already_taken(self, mock_input):
        self.board[1][1] = "X"  # Simule une case déjà prise
        with patch('sys.stdout', new=StringIO()) as fake_out:
            tic_tac_toe()
            output = fake_out.getvalue()
        self.assertIn("That spot is already taken! Try again.", output)


    def tearDown(self):
        # Nettoyage après chaque test (si nécessaire)
        pass

if __name__ == "__main__":
    unittest.main()
