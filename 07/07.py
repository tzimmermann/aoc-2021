f = open('07/input.txt', 'r')

crabs = [int(char.strip()) for char in f.readlines()[0].split(',')]

maxCrab = max(crabs)

# Part 1
positionCosts = []

for position in range(maxCrab + 1):
    positionCosts.append(sum((abs(crab - position) for crab in crabs)))

minCost = min(positionCosts)
minCostPosition = positionCosts.index(minCost)
print('Minimal cost is ' + str(minCost) + ' at position ' + str(minCostPosition))

# Part 2
positionCosts = []

for position in range(maxCrab + 1):
    cost = 0
    for crab in crabs:
        positionDiff = abs(crab - position)
        # Sum of first N numbers
        cost += (positionDiff * (positionDiff + 1)) // 2
    positionCosts.append(cost)

minCost = min(positionCosts)
minCostPosition = positionCosts.index(minCost)
print('Minimal cost is ' + str(minCost) + ' at position ' + str(minCostPosition))