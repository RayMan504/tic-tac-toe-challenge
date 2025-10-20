# TODO: Generate three by three grid
board = [["", "", ""], ["", "", ""], ["", "", ""]]
# TODO: User can place X and 0 on grid
row = input("Select Row ")
column = input("Select Column ")
board[int(row)][int(column)] = "X"
# TODO: make sure board persists values
# TODO: Track user input when placed on grid
# TODO: Validate win conditions 
print(board)