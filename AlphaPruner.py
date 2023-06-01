# TIC TAC TOE BOT

print("Welcome to Tic Tac Toe")
print()

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    print()
    for x in range(rows):
        print("+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
        print()
    print("+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn

def checkForWinner(gameBoard):
    for i in range(rows):
        # Check rows
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2]:
            return gameBoard[i][0]

        # Check columns
        if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i]:
            return gameBoard[0][i]

    # Check diagonals
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    return None

def checkIfBoardFull(gameBoard):
    for x in range(rows):
        for y in range(cols):
            if isinstance(gameBoard[x][y], int):
                return False
    return True

def minimax(gameBoard, depth, maximizingPlayer):
    if checkForWinner(gameBoard) == "X":
        return -1
    elif checkForWinner(gameBoard) == "O":
        return 1
    elif checkIfBoardFull(gameBoard):
        return 0

    if maximizingPlayer:
        maxEval = float('-inf')
        for x in range(rows):
            for y in range(cols):
                if isinstance(gameBoard[x][y], int):
                    gameBoard[x][y] = 'O'
                    eval = minimax(gameBoard, depth + 1, False)
                    gameBoard[x][y] = x * cols + y + 1
                    maxEval = max(eval, maxEval)
        return maxEval
    else:
        minEval = float('inf')
        for x in range(rows):
            for y in range(cols):
                if isinstance(gameBoard[x][y], int):
                    gameBoard[x][y] = 'X'
                    eval = minimax(gameBoard, depth + 1, True)
                    gameBoard[x][y] = x * cols + y + 1
                    minEval = min(eval, minEval)
        return minEval

def getBestMove(gameBoard):
    bestEval = float('-inf')
    bestMove = None
    alpha = float('-inf')
    beta = float('inf')
    for x in range(rows):
        for y in range(cols):
            if isinstance(gameBoard[x][y], int):
                gameBoard[x][y] = 'O'
                eval = minimax(gameBoard, 0, False)
                gameBoard[x][y] = x * cols + y + 1
                if eval > bestEval:
                    bestEval = eval
                    bestMove = x * cols + y + 1
    return bestMove


leaveLoop = False
turnCounter = 0

while not leaveLoop:
    if turnCounter % 2 == 0:
        printGameBoard()
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if numberPicked in possibleNumbers:
            modifyArray(numberPicked, 'X')
            possibleNumbers.remove(numberPicked)
            turnCounter += 1
    else:
        cpuChoice = getBestMove(gameBoard)
        print("\nCpu choice:", cpuChoice)
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1

    winner = checkForWinner(gameBoard)
    if winner:
        printGameBoard()
        print("\nGame over! Winner:", winner)
        leaveLoop = True
    elif checkIfBoardFull(gameBoard):
        printGameBoard()
        print("\nGame over! It's a tie!")
        leaveLoop = True
