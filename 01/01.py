import functools

f = open('input.txt', 'r')
prev_sea_floor_depth = None
increases_count = 0

# Naive using for-loop
for line in f:
    # print(line, end="")
    sea_floor_depth = int(line)
    if (prev_sea_floor_depth is not None and sea_floor_depth > prev_sea_floor_depth):
        increases_count += 1

    prev_sea_floor_depth = sea_floor_depth

print(increases_count)

# Back to start of file
f.seek(0)

# Functional w/ reduce
def countIncreases(prev, curr):
    curr_sea_floor_depth = int(curr)
    return {
        "sea_floor_depth": curr_sea_floor_depth,
        "increases_count": prev["increases_count"]+1 if (prev["sea_floor_depth"] is not None and curr_sea_floor_depth > prev["sea_floor_depth"]) else prev["increases_count"]
    }

func_increases = functools.reduce(countIncreases, f, {"increases_count": 0, "sea_floor_depth": None })

print(func_increases["increases_count"])


# Back to start of file
f.seek(0)

# Functional w/ list comprehension

depths = [int(line) for line in f]
increases = [1 if depths[lineNumber+1] > depths[lineNumber] else 0 for lineNumber in range(len(depths)-1)]
print(sum(increases))

# Part 2

triplets = [(depths[lineNumber], depths[lineNumber+1], depths[lineNumber+2]) for lineNumber in range(len(depths)-2)]
increases = [1 if sum(triplets[i+1]) > sum(triplets[i]) else 0 for i in range(len(triplets)-1)]
print(sum(increases))

