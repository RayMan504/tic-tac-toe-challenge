# TODO: make sure board persists values
class TicTacToe:
    # Generate three by three grid
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    #TODO: start game
    def startTurn(self):
        #TODO: prompt player to make move
        row = input("Choose Row Number: 1-3 ")
        column = input("Choose Column Number: 1-3 ")
        #TODO call method to place X or O on board
        self.makeMove(int(row) - 1, int(column) -1)
    # TODO: User can place X and 0 on grid
    def makeMove(self, row, column):
        self.board[row][column] = "X"
        print(self.board)
        self.startTurn()
        # TODO: Track user input when placed on grid
    # TODO: Validate win conditions 
