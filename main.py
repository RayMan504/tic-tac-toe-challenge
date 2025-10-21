class TicTacToe:
    #start game on init
    def __init__(self):
        # prompt player names and assign X and O
        piece = input("Player 1 is X or O? ")
        self.piece = piece
        # Generate three by three grid
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.startTurn(self.piece)

    def startTurn(self, player):
        #prompt player to make move
        row = input("Choose Row Number: 1-3 ")
        column = input("Choose Column Number: 1-3 ")
        #all method to place X or O on board
        self.makeMove(int(row) - 1, int(column) -1, player)
    # TODO: User can place X and 0 on grid
    def makeMove(self, row, column, player):
        # Track user input when placed on grid
        # if space occupied
        if self.board[row][column] != "":
            # display message
            print("Space occupied. Try again")
            # redo turn
            self.startTurn(self.piece)

        # after adding new space update piece
        if player == "X":
            self.board[row][column] = "X"
            self.piece = "O"
        else:
            self.board[row][column] = "0"
            self.piece = "X"
        print(self.board)
        self.startTurn(self.piece)
    # TODO: Validate win conditions 
        # validate three ways
        # iterate horizontally
            # verify win condition
        # iterate vertically
            # verify win condition 
        # iterate diagonally
            # verify win condition
        # if condition met
            # end the game   
    # TODO: end the game  

newGame = TicTacToe()