import functools

f = open('02/input.txt', 'r')

# Part 1
position = {"horizontal": 0, "depth": 0}

def followInstructions(position, instruction):
    [direction, units] = instruction.split()
    if (direction == "forward"):
        position["horizontal"] += int(units)
    elif (direction == "up"):
        position["depth"] -= int(units)
    elif (direction == "down"):
        position["depth"] += int(units)
    else:
        raise ValueError('Unknown instruction: ' + direction)
    return position

functools.reduce(followInstructions, f, position)

print(position)
print(position["horizontal"] * position["depth"])

f.seek(0)

# Part 2

position = {"horizontal": 0, "depth": 0, "aim": 0}

def followInstructions(position, instruction):
    [direction, units] = instruction.split()
    if (direction == "forward"):
        position["horizontal"] += int(units)
        position["depth"] += position["aim"] * int(units)
    elif (direction == "up"):
        position["aim"] -= int(units)
    elif (direction == "down"):
        position["aim"] += int(units)
    else:
        raise ValueError('Unknown instruction: ' + direction)
    return position

functools.reduce(followInstructions, f, position)

print(position)
print(position["horizontal"] * position["depth"])