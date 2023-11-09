# Domineering-game
Explanation of functions used in the project: 

1.	DrawTable(row, column, matrix)
Plot a table in the console. 
Row - Number of species
Column - Number of columns
Matrix – current state of the board (memory of occupied and free positions). Each field of this matrix (list list) is a bluple in which the first data remembers information about whether it is a human(0) or a computer (1) (initially 2) and the second data its designation ("X" or "O") (initially " ").

2.	CreateMatrix(row, column)
Defining a matrix to remember the state of the table.

3.	IsValidMove(move, matrix, player, column, row)
Check if the tile is off the board, that it does not stick out of the board, and that it does not match any of the tiles already placed. 
Move – a tuple in which the first data is a type number and the second is the column label of a particular stroke
Player — a tuple in which the first data remembers information about whether it is a human or a computer, and the second data its tag ("X" or "O"). "X" always plays first.

4.	PlayMove(matrix, player, move, column, row)
Function for playing moves (filling the corresponding positions on the board (parameter move) played by the player who is in line).

5.	InputMoveValidation(input)
Validate an entry.
Input – a string entered by the user when playing a move. It must be the shape of the <type><space><column>

6.	ConvertInputMove(input)
Converting from string to tuple. Tuple is actually a parameter of the other functions in which it occurs.

7.	EndGame(matrix, player, column, row)
Function to check the end game.

8.	StartGame()
Main function

9.	AvailableMoves (matrix, player, column, row )
A function to determine all possible moves of a particular player. 
As part of this function, the boards are drawn with all possible strokes, one by one. The return value of this function is a list of tuples that represent all possible moves. 

10.	 DeleteMove (matrix, move, player, row)
Function to delete a specific move (move) of a specific player. This function is called within the AvailableMove function. 

