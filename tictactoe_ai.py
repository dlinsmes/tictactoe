
#don't need to declare variables
board = []

piece = "o"
moveRow = -1
moveCol = -1

#define a function
def main():
    setupBoard()
    printBoard()

    while not winner() and not tie():
        changePiece()
        makeMove()
        printBoard()

def setupBoard():
    #for loop that iterates from 0 to 2
    for i in range(3):
        #declare row as a list
        row = []
        for j in range(3):
            row.append("_")
        board.append(row)

def printBoard():
    #for each loop
    for row in board:
        # print(row)
        line = ""
        for pos in row:
            line += pos + "  "
        print(line)
    print()

def tie():
    #look for blanks and if there are any, return false
    #otherwise return true
    for row in board:
        for i in row:
            if i == "_":
                return False
    print("Tie game!")
    return True

def winner():
    rowCount = 0
    colCount = 0
    diag1Count = 0
    diag2Count = 0
    for i in range(3):
        if board[i][moveCol] == piece:
            colCount += 1
        if board[moveRow][i] == piece:
            rowCount += 1
        if board[i][i] == piece:
            diag1Count += 1
        #len(board) to get length of board
        if board[i][len(board)-1-i] == piece:
            diag2Count += 1

    if rowCount == 3 or colCount == 3 or diag1Count == 3 or diag2Count == 3:
        print(piece + " wins!")
        return True

    return False

def changePiece():
    #specify you're using a global variable
    #(like a java class variable)
    #signs: unresolved reference error
    # or shadows name warning
    global piece

    if piece == "o":
        piece = "x"
    else:
        piece = "o"

def makeMove():
    global moveRow
    global moveCol

    #user is x
    if piece == "x":

        print(piece + "'s turn")
        #input defaults to String so cast to int
        moveRow = int(input("Enter row: "))
        moveCol = int(input("Enter col: "))
        while moveRow < 0 or moveRow >= 3 or moveCol < 0 or moveCol >= 3 or board[moveRow][moveCol] != "_":
            print("invalid move")
            moveRow = int(input("Enter row: "))
            moveCol = int(input("Enter col: "))

    else:
        #python functions can return multiple values
        moveRow, moveCol = ai_turn()


    board[moveRow][moveCol] = piece

def ai_turn():
    row = -1
    col = -1

    return row, col

#make sure to call main() at the bottom
main()