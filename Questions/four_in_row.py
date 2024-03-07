import sys
PLAYER_X = "X"
PLAYER_O = "O"

WIDTH = 7
HEIGHT = 6
EMPTY_SPACE = "."
COLUMN_LABELS = ("1","2","3","4","5","6","7")
assert len(COLUMN_LABELS)==WIDTH

# the following creates the template in an ascii art 

# BOARD_TEMPLATE = """
    #  1234567
    # +-------+
    # |{}{}{}{}{}{}{}|
    # |{}{}{}{}{}{}{}|
    # |{}{}{}{}{}{}{}|
    # |{}{}{}{}{}{}{}|
    # |{}{}{}{}{}{}{}|
    # |{}{}{}{}{}{}{}|
    # +-------+"""
# the above is equivalent of the following

EDGE = "+"+("-"*WIDTH)+"+"
ROW = "|"+("{}"*WIDTH)+"|\n"
template = "\n     " + "".join(COLUMN_LABELS) + "\n" + EDGE + "\n" + (ROW * HEIGHT) +EDGE
# print(template)

def getnewgameboard():
    board = {}
    for rowindex in range(HEIGHT):
        for columnindex in range(WIDTH):
            board[(columnindex,rowindex)]= EMPTY_SPACE
    return board

def displayboard(board):
    """to display board and tiles"""
    displaytile = []
    for rowindex in range(HEIGHT):
        for columnindex in range(WIDTH):
            displaytile.append(board[(columnindex,rowindex)])
    print(template.format(*displaytile))

def getPlayerMove(playerTile, board):
    while True:  # Keep asking player until they enter a valid move.
        print(f"Player {playerTile}, enter 1 to {WIDTH} or QUIT:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Enter a number from 1 to {WIDTH}.")
            continue  

        columnIndex = int(response) - 1  

        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("That column is full, select another one.")
            continue  # Ask player again for their move.

        for rowIndex in range(HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)

def isFull(board):
    for rowIndex in range(HEIGHT):
        for columnIndex in range(WIDTH):
            if board[(WIDTH,HEIGHT)]==EMPTY_SPACE:
                return False
    return True

# to determine the winner there needs to be four tiles together
def isWinner(playerTile,board):
    # check four tiles going right
    for columnIndex in(WIDTH-3):
        for rowIndex in (HEIGHT):
            tile_1 = board[(columnIndex,rowIndex)]
            tile_2 = board[(columnIndex +1,rowIndex)]
            tile_3 = board[(columnIndex +2,rowIndex)]
            tile_4 = board[(columnIndex +3,rowIndex)]
            if tile_1==tile_2==tile_3==tile_4 == playerTile:
                return True
            
     # check four tiles going down
    for columnIndex in(WIDTH):
        for rowIndex in (HEIGHT-3):
            tile_1 = board[(columnIndex,rowIndex)]
            tile_2 = board[(columnIndex,rowIndex +1)]
            tile_3 = board[(columnIndex,rowIndex +2)]
            tile_4 = board[(columnIndex,rowIndex +3)]
            if tile_1==tile_2==tile_3==tile_4 == playerTile:
                return True
            
    # check four tiles going right diagonal
    for columnIndex in(WIDTH-3):
        for rowIndex in (HEIGHT-3):
            tile_1 = board[(columnIndex,rowIndex)]
            tile_2 = board[(columnIndex +1,rowIndex +1)]
            tile_3 = board[(columnIndex +2,rowIndex +2)]
            tile_4 = board[(columnIndex +3,rowIndex +3)]
            if tile_1==tile_2==tile_3==tile_4 == playerTile:
                return True
            
       # check four tiles going left diagonal
    for columnIndex in(WIDTH-3):
        for rowIndex in (HEIGHT-3):
            tile_1 = board[(columnIndex +3,rowIndex)]
            tile_2 = board[(columnIndex +2,rowIndex +1)]
            tile_3 = board[(columnIndex +1,rowIndex +2)]
            tile_4 = board[(columnIndex,rowIndex +3)]
            if tile_1==tile_2==tile_3==tile_4 == playerTile:
                return True        

def main():
    # Set up a new game:
    gameBoard = getnewgameboard()
    playerTurn = PLAYER_X

    while True:  # Run a player's turn.
        # Display the board and get player's move:
        displayboard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # Check for a win or tie:
        if isWinner(playerTurn, gameBoard):
            displayboard(gameBoard)  
            print("Player {} has won!".format(playerTurn))
            sys.exit()
            
        elif isFull(gameBoard):
            displayboard(gameBoard)
            print("There is a tie!")
            sys.exit()

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X
        
if __name__=="__main__":
    main()