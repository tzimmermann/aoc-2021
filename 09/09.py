import copy
from functools import reduce

f = open('09/input.txt', 'r')

grid = [[int(char) for char in line.strip()] for line in f.readlines()]

X_DIMENSION = len(grid[0])
Y_DIMENSION = len(grid)

def collectNeighbors(point, grid):
    (pointX, pointY) = point
    candidates = [
        (pointX, pointY - 1),
        (pointX + 1, pointY),
        (pointX, pointY + 1),
        (pointX - 1, pointY)
    ]
    neighbors = []
    for (candidateX, candidateY) in candidates:
        if candidateX < 0 or candidateY < 0 or candidateX >= X_DIMENSION or candidateY >= Y_DIMENSION:
            # Skip out-of-bounds candidates
            continue
        else:
            neighbors.append(grid[candidateY][candidateX])
    return neighbors

def isLowPoint(point, grid):
    (pointX, pointY) = point
    pointHeight = grid[pointY][pointX]
    neighbors = collectNeighbors((pointX, pointY), grid)
    smallerNeighbors = [neighbor for neighbor in neighbors if neighbor <= pointHeight]
    return not smallerNeighbors

lowPoints = [(x, y) for x in range(X_DIMENSION) for y in range(Y_DIMENSION) if isLowPoint((x, y), grid)]
riskLevelSum = sum(grid[y][x] + 1 for (x,y) in lowPoints)
print("Risk level sum: " + str(riskLevelSum))

basins = [[None for x in range(X_DIMENSION)] for y in range(Y_DIMENSION)]

# Remove height=9 straight away, they are not in any basins
pointsWithoutBasin = [(x, y) for y in range(Y_DIMENSION) for x in range(X_DIMENSION) if grid[y][x] < 9]
currentBasin = 0

def getAdjacentBasin(point, basins):
    neighboringBasins = [basin for basin in collectNeighbors(point, basins) if basin is not None]
    if neighboringBasins:
        # Important to always to choose one particular basin, otherwise the algorithm will not converge
        # and instead keep changing the grid infinitely.
        return max(neighboringBasins)
    return None


def printGrid(grid):
    for row in grid:
        print("".join(str([0 if char is None else char for char in row])))


def hasGridChanged(oldGrid, newGrid):
    for y in range(Y_DIMENSION):
        for x in range(X_DIMENSION):
            if oldGrid[y][x] != newGrid[y][x]:
                return True
    return False

basinsChanged = True

while basinsChanged:
    oldBasins = copy.deepcopy(basins)

    for currentPoint in pointsWithoutBasin:
        (pointX, pointY) = currentPoint
        height = grid[pointY][pointX]

        adjacentBasin = getAdjacentBasin(currentPoint, basins)
        if not adjacentBasin:
            # open new basin
            currentBasin += 1
            basins[pointY][pointX] = currentBasin
        else:
            basins[pointY][pointX] = adjacentBasin

    basinsChanged = hasGridChanged(oldBasins, basins)

def countBasins(grid):
    basinIndices = [char for row in grid for char in row if char is not None]
    maxIndex = max(basinIndices)
    basinSizes = dict()
    for i in range(1, maxIndex + 1):
        indexCount = basinIndices.count(i)
        basinSizes[i] = indexCount

    topThree = sorted(basinSizes.items(), key=lambda item: item[1], reverse=True)[:3]
    productOfTopThree = reduce((lambda product,basin: product * basin[1]), topThree, 1)
    print(productOfTopThree)

countBasins(basins)
