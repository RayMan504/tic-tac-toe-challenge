import random


class TicTacToe:
    #start game on init
    def __init__(self):
        self.piece = "X"
        # Generate three by three grid
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.hasPlayerWon = False

        print(self.drawBoard())
        self.startTurn()

    # draw board to render to user
    def drawBoard(self):
        rendered_rows = []
        for row in self.board:
            rendered_rows.append("| " + " | ".join(cell if cell else " " for cell in row) + " |")
        return "\n".join(rendered_rows)

    def startTurn(self):
        if self.piece == "X":
            # prompt player to make move
            row = input(f"Player {self.piece} Choose Row Number: 1-3 ")
            column = input(f"Player {self.piece} Choose Column Number: 1-3 ")

            # figure out how to negate non numbers
            if(row.isdigit() == False or column.isdigit() == False):
                print("Input must be a number!")
                self.startTurn()
                return
            #all method to place X or O on board
            self.makeMove(int(row) - 1, int(column) -1, self.piece)
            return

        self.computerMove()

    def getAvailableMoves(self):
        return [(row, column) for row in range(3) for column in range(3) if self.board[row][column] == ""]

    def getWinningMove(self, player):
        for row, column in self.getAvailableMoves():
            self.board[row][column] = player
            if self.checkForWinner(player):
                self.board[row][column] = ""
                return row, column
            self.board[row][column] = ""
        return None

    def checkForWinner(self, player):
        previousPiece = self.piece
        self.piece = player
        self.checkHorizontal()
        self.checkVertical()
        self.checkDiagonal()
        hasWinner = self.hasPlayerWon
        self.hasPlayerWon = False
        self.piece = previousPiece
        return hasWinner

    def computerMove(self):
        availableMoves = self.getAvailableMoves()

        if not availableMoves:
            return

        # 1. Take an immediate win if available.
        winningMove = self.getWinningMove(self.piece)
        if winningMove is not None:
            row, column = winningMove
        else:
            # 2. Block the player's immediate win.
            opponent = "X" if self.piece == "O" else "O"
            blockMove = self.getWinningMove(opponent)
            if blockMove is not None:
                row, column = blockMove
            else:
                # 3. Prefer the center, then corners, then remaining open spaces.
                preferredMoves = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)]
                row, column = next(((r, c) for r, c in preferredMoves if (r, c) in availableMoves), random.choice(availableMoves))

        print(f"Computer plays {self.piece} at row {row + 1}, column {column + 1}")
        self.makeMove(row, column, self.piece)

    # User can place X and 0 on grid
    def makeMove(self, row, column, player):
        # handle out of range coordinates
        if(row < 0 or row > 2 or column > 2 or column < 0):
            print("Out of board range! Try again.")
            self.startTurn()
            return
        # Track user input when placed on grid
        # if space occupied
        if self.board[row][column] != "":
            # display message
            print("Space occupied! Try again.")
            # redo turn
            self.startTurn()
            return

        self.board[row][column] = player
        print(self.drawBoard())
        self.checkWinConditions()

    # Validate win conditions
    def conditionValidator(self, rowOrColumn):
        # check if all values match set of Xs or Os
        return all(space == self.piece for space in rowOrColumn)
    
    def checkWinConditions(self):
        # validate three ways
        self.checkHorizontal()
        self.checkVertical()
        self.checkDiagonal()

        # if a player has won
        if self.hasPlayerWon:
            # end the game
            self.endGame()


        # check for draw
        elif self.hasPlayerWon == False and self.checkIfEntireBoardPopulated() == True:
            self.endGame()
        else:
            # toggle piece
            self.piece = "O" if self.piece == "X" else "X"
            self.startTurn()

    def checkHorizontal(self):
        # iterate horizontally
        for row in self.board:
            # verify win condition: do all values in row match
            if self.conditionValidator(row) == True:
                self.hasPlayerWon = True

    def checkVertical(self):
        # iterate vertically: loop numbers 0 - 3
        for i in range(3):
            # find a way to only grab same index in each row
            column = [row[i] for row in self.board]
            if self.conditionValidator(column):
                self.hasPlayerWon = True

    # iterate diagonally
    def checkDiagonal(self):
        # we know that in tic tac toe only two possible win conditions for diagonals
        diagonalOne = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonalTwo = [self.board[0][2], self.board[1][1], self.board[2][0]]
        # validate
        if self.conditionValidator(diagonalOne) or self.conditionValidator(diagonalTwo):
            self.hasPlayerWon = True

    def checkIfEntireBoardPopulated(self):
        # verify if all pieces places on board (try to flatten?)
        # flatten
        flattenedBoard = [space for row in self.board for space in row]
        return all(space != "" for space in flattenedBoard)
    
    # end the game 
    def endGame(self):
        print(f"Player {self.piece} wins!") if self.hasPlayerWon else print(f"Match Draw!")
        return


if __name__ == "__main__":
    TicTacToe()