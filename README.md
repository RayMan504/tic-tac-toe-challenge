# tic-tac-toe-challenge
fun two player tic tac toe game written in python


## How to Start Game

```bash
python3 main.py# Tic-Tac-Toe Challenge

A simple two-player Tic-Tac-Toe game built with Python and played directly from the command line.

## Features

* Generates a 3×3 Tic-Tac-Toe board
* Supports two players using **X** and **O**
* Prompts players to select a board position
* Validates player input and board coordinates
* Prevents players from selecting an occupied space
* Checks for winning combinations after every move
* Automatically switches turns after a valid move
* Detects when a player wins and ends the game
* Handles invalid coordinates and out-of-range input
* Supports single-digit board positions within the 3×3 board

## Requirements

* Python 3.x

## How to Start

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/tic-tac-toe-challenge.git
cd tic-tac-toe-challenge
```

Run the game with:

```bash
python3 main.py
```

Or, on systems where `python` points to Python 3:

```bash
python main.py
```

## How to Play

1. The game generates a 3×3 board.
2. Players take turns placing their assigned piece (`X` or `O`).
3. Enter the number corresponding to the position where you want to place your piece.
4. The game validates your selection.
5. After each valid move, the game checks for a winner.
6. If there is no winner, the turn switches to the other player.
7. The game ends when a player gets three pieces in a row.

## Example Board

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Players select a position by entering its corresponding number.

## Project Structure

```text
tic-tac-toe-challenge/
├── main.py
└── README.md
```

## Purpose

This project was created as a Python programming challenge focused on:

* Conditional logic
* Loops
* Functions
* User input validation
* State management
* Board manipulation
* Game logic

```
or
```bash
python main.py
```

## FEATURES
* Generate Board
* Assigns tic tac toe pieces (X or O)
* User prompted to place piece on board
* Win conditions are checked after new piece placed on board
* If no winner after turn, next turn player is toggled
* User re prompted to place piece if occupied or placement outside of range
* If there is a winner, displays message and ends the game
* Handle user coordinate constraints (only single digits withint 3x3 board range)
