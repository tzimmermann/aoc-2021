import itertools

f = open('08/input.txt', 'r')

signals = [lineSplit.strip().split(' ') for line in f.readlines() for lineSplit in line.split(' | ')]

patterns = [signal for (index, signal) in enumerate(signals) if index % 2 == 0]
outputs = [signal for (index, signal) in enumerate(signals) if index % 2 == 1]

uniqueSegementCounts = [2, 3, 4, 7]

flatOutputs = [item for output in outputs for item in output]

# Part 1
print(sum(1 if len(output) in uniqueSegementCounts else 0 for output in flatOutputs))

# Part 2
segmentNumberMap = {
    "012456": 0,
    "25": 1,
    "02346": 2,
    "02356": 3,
    "1235": 4,
    "01356": 5,
    "013456": 6,
    "025": 7,
    "0123456": 8,
    "012356": 9
}

def checkMapping(mapping, pattern):
    segmentIndices = [(mapping.index(letter)) for letter in pattern]
    segmentIndices.sort()
    segmentKey = "".join(str(segmentIndex) for segmentIndex in segmentIndices)
    if segmentKey in segmentNumberMap:
        return segmentNumberMap[segmentKey]
    return None

def crackOutput(mapping, output):
    crackedOutputs = []
    for oneOutput in output:
        crackedOutput = checkMapping(mapping, oneOutput)
        if crackedOutput is None:
            raise ValueError
        else:
            crackedOutputs.append(crackedOutput)
    return int("".join(str(outputNumber) for outputNumber in crackedOutputs))
        
outputValues = []

for i in range(len(outputs)):
    output = outputs[i]
    pattern = patterns[i]

    for permutation in itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]):
        permutationIsValid = True
        for onePattern in pattern:
            number = checkMapping(permutation, onePattern)
            if number is None:
                permutationIsValid = False
                break
        if permutationIsValid:
            outputValues.append(crackOutput(permutation, output))
            break

print(sum(outputValues))