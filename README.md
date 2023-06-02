# Tic Tac Toe Bot

[![Python](https://img.shields.io/badge/Python-Algorithmic%20Solving-blue)](https://www.python.org)

Created a Tic Tac Toe game implementation with an AI bot that uses the minimax algorithm with alpha-beta pruning to make optimal moves. The bot is designed to never lose in Tic Tac Toe. Below is a brief overview of the code structure and how the game works.

# Game Board Representation
The game board is represented using a 2D list called gameBoard. Each cell in the board holds either a number from 1 to 9 (representing an empty position) or 'X' or 'O' (representing player moves). The board is printed to the console after each move.

![Image Alt Text](/StartScreen.jpeg)

# Functions
printGameBoard(): Prints the current state of the game board.

modifyArray(num, turn): Modifies the game board based on the player's move.

checkForWinner(gameBoard): Checks if there is a winner by checking rows, columns, and diagonals.

checkIfBoardFull(gameBoard): Checks if the game board is full (no more empty positions).

minimax(gameBoard, depth, maximizingPlayer): The minimax algorithm with alpha-beta pruning. Evaluates the game board positions and returns the best possible score for the current player.

getBestMove(gameBoard): Determines the best move for the AI player ('O') using the minimax algorithm.

# Game Loop
The game loop continues until a winner is found or the game board is full (tie). The loop alternates between the human player ('X') and the AI player ('O'). The human player chooses a number from 1 to 9 to make a move, and the AI player uses the getBestMove() function to determine its move. The game board is updated after each move.

# End of Game
After each move, the code checks for a winner using the checkForWinner() function. If a winner is found, the game ends, and the winner is displayed. If the game board is full and no winner is found, the game ends in a tie.

# How to Use
Run the code in a Python environment.
Follow the prompts to make your moves by choosing a number from 1 to 9.
The AI bot will automatically make its moves.
The game ends when there is a winner or a tie.
Enjoy playing Tic Tac Toe against the unbeatable AI bot!
Please note that this code assumes the user will input valid moves (numbers from 1 to 9) and doesn't include extensive input validation. Feel free to enhance the code further to add input validation or improve the user interface as per your requirements.

Have fun playing Tic Tac Toe! (This will not be fun if you enjoy winning)
