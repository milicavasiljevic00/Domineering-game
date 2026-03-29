# Domino game with AI

This project is a console-based turn-based board game implemented in Python.  
The game supports a human player and a computer player, with the computer making decisions using the **Minimax algorithm** with **alpha-beta pruning**.

## Features

- Dynamic board creation based on user-defined dimensions
- Console-based board rendering
- Input validation for player moves
- Support for two different piece placements:
  - **X** pieces are placed vertically
  - **O** pieces are placed horizontally
- Endgame detection based on available valid moves
- AI opponent using:
  - Minimax search
  - Alpha-beta pruning
  - Heuristic state evaluation

## How it works

The game starts by asking the user to enter:
- the number of rows
- the number of columns
- whether the first player is the human or the computer

The board is then created and displayed in the console.

Players take turns placing pieces on the board:
- Player **X** places pieces vertically
- Player **O** places pieces horizontally

The game ends when the current player has no valid moves left.  
The other player is declared the winner.

## Project structure

The project includes functions for:

- creating and displaying the board
- validating and converting user input
- checking whether a move is valid
- placing and removing moves
- generating all available moves
- evaluating board states
- running the Minimax algorithm with alpha-beta pruning
- managing the game loop
