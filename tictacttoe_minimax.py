
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

     #runs after game is over
    if tie():
        print("tie game")
    elif piece == "x":
        print("x wins!")
    else:
        print("o wins")

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
    # print("Tie game!")
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
        # print(piece + " wins!")
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
        moveRow, moveCol = ai_turn()

    board[moveRow][moveCol] = piece

def ai_turn():

    global moveRow
    global moveCol
    global piece

    #look at all possible moves and determine which one is best - choose the
    #one with the highest score
    bestRow = -1
    bestCol = -1

    bestScore = -100

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":

                #so winner() function can evaluate where piece is placed
                moveRow = i
                moveCol = j

                #simulate placing the piece to evaluate what happens
                board[i][j] = "o"

                moveScore = evaluate(False)

                #undo the move
                board[i][j] = "_"

                if moveScore > bestScore:
                    bestRow = i
                    bestCol = j
                    bestScore = moveScore

    #piece is used in winner()
    piece = "o"

    return bestRow, bestCol

#param is a boolean for whose turn is next
def evaluate(isAITurnNext):
    global moveRow
    global moveCol
    global piece

    #user won
    if isAITurnNext and winner():
        return -1

    #ai won
    if not isAITurnNext and winner():
        return 1

    if tie():
        return 0

    #another player still needs to go

    #simulate ai's next move
    if isAITurnNext:
        #maximize best score
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    moveRow, moveCol, piece = i, j, "o"
                    board[i][j] = "o"
                    moveScore = evaluate(not isAITurnNext)
                    board[i][j] = "_"
                    if moveScore > bestScore:
                        bestScore = moveScore
        return bestScore

    # simulate other player going next
    else:
        #other player is minimizing AI's score
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    moveRow, moveCol, piece = i, j, "x"
                    board[i][j] = "x"
                    moveScore = evaluate(not isAITurnNext)
                    board[i][j] = "_"
                    if moveScore < bestScore:
                        bestScore = moveScore
        return bestScore



    #make sure to call main() at the bottom
main()