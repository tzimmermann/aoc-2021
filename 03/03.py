import operator

f = open('03/input.txt', 'r')

# Part 1

bitCounts = [[0, 0] for x in range(12)]

for line in f:
    for charIndex, char in enumerate(line):
        if (char == '\n'):
            continue
        bit = int(char)
        bitCounts[charIndex][bit] += 1

mostCommon = ['0' if bitCount[0] > bitCount[1] else '1' for bitCount in bitCounts]
leastCommon = ['0' if bitCount[0] < bitCount[1] else '1' for bitCount in bitCounts]
gammaRate = int(''.join(mostCommon), 2)
epsilonRate = int(''.join(leastCommon), 2)

print(gammaRate * epsilonRate)

f.seek(0)

# Part 2

# Removing trailing newlines
lines = [line.strip() for line in f.readlines()]

def countBitsAtPlace(lines, place):
    bitColumn = [line[place] for line in lines]
    return (bitColumn.count('0'), bitColumn.count('1'))

def filterLines(lines, place, targetBit):
    return [line for line in lines if line[place] == targetBit]

def calculateRating(operator):
    filteredLines = lines.copy()
    currentPlace = 0
    while len(filteredLines) > 1:
        counts = countBitsAtPlace(filteredLines, currentPlace)
        filterBit = '0' if operator(counts[0], counts[1]) else '1'
        filteredLines = filterLines(filteredLines, currentPlace, filterBit)
        currentPlace += 1
    return int(filteredLines[0], 2) 

def calculateOxygen():
    return calculateRating(operator.gt)

def calculateCO2():
    return calculateRating(operator.le)

print(calculateOxygen() * calculateCO2())
