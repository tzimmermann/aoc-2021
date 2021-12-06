f = open('04/input.txt', 'r')

lines = f.readlines()

drawings = [int(draw) for draw in lines[0].split(',')]

def parseBoard(startLineIndex):
    dimension = 5
    horizontalLines = [list(map(int, line.split())) for line in lines[startLineIndex:startLineIndex + dimension]]
    # Transpose matrix to get vertical bingo lines
    verticalLines = [[horizontalLines[row][col] for row in range(0, dimension) ] for col in range(0, dimension) ]
    
    horizontalLines.extend(verticalLines)

    # Sets make it easier to remove items and we don't care about the order inside a row/column
    return [set(oneLine) for oneLine in horizontalLines]

boards = [parseBoard(lineIndex) for lineIndex in range(2, len(lines), 6)]

def markNumber(board, number):
    for line in board:
        line.discard(number)

    # An empty line means BINGO. Empty lists are falsy, we keep falsy lines in a new list.
    # If we have anything left in the new list (aka the new list is truthy), we have at least one BINGO.
    hasBingo = bool([line for line in board if not line])

    return None if not hasBingo else sum(set().union(*board))

# Part 1

def checkFirstWinningBoard():
    for drawnNumber in drawings:
        for board in boards:
            bingoSum = markNumber(board, drawnNumber)
            if (bingoSum is not None):
                print('Bingo after number ' + str(drawnNumber) + ' with sum ' + str(bingoSum) + ' result: ' + str(drawnNumber * bingoSum))
                break
        if (bingoSum is not None):
            break
        
checkFirstWinningBoard()

# Part 2

def checkLastWinningBoard():
    currentBoards = boards
    for drawnNumber in drawings:
        boardsToRemove = []
        for board in currentBoards:
            bingoSum = markNumber(board, drawnNumber)
            if (bingoSum is not None):
                print('Bingo after number ' + str(drawnNumber) + ' with sum ' + str(bingoSum) + ' result: ' + str(drawnNumber * bingoSum))
                boardsToRemove.append(board)
        currentBoards = [board for board in currentBoards if not board in boardsToRemove]

checkLastWinningBoard()