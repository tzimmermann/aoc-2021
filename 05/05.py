f = open('05/input.txt', 'r')

def generateLines(file, keepDiagonals = False):
    lines = []
    for line in file:
        point1, point2 = line.split(' -> ')
        x1, y1 = list(map(lambda p: int(p.strip()), point1.split(',')))
        x2, y2 = list(map(lambda p: int(p.strip()), point2.split(',')))
        if x1 == x2 or y1 == y2 or keepDiagonals:
            # Make sure the smaller point comes first
            if x2 < x1 or y2 < y1:
                (x1, x2) = (x2, x1)
                (y1, y2) = (y2, y1)
            lines.append({"x1": x1, "y1": y1,"x2": x2, "y2": y2})
    return lines

def printGrid(grid):
    for row in grid:
        rowStrings = [str(count) if count > 0 else "." for count in row]
        print("".join(rowStrings))

def getGridCounts(lines):
    overallMaxX = max(map(lambda line:  max(line["x1"], line["x2"]), lines))
    overallMaxY = max(map(lambda line:  max(line["y1"], line["y2"]), lines))

    grid = [[0 for x in range(overallMaxX + 1)] for y in range(overallMaxY + 1)]

    for line in lines:
        if line["x1"] != line["x2"] and line["y1"] != line["y2"]:
            # We have a diagonal line!
            xstep = 1 if line["x1"] <= line["x2"] else -1
            ystep = 1 if line["y1"] <= line["y2"] else -1
            points = zip(range(line["x1"], line["x2"] + xstep, xstep), range(line["y1"], line["y2"] + ystep, ystep))
            for (x, y) in points:
                grid[y][x] += 1
        else:
            for x in range(line["x1"], line["x2"] + 1):
                for y in range(line["y1"], line["y2"] + 1):
                    grid[y][x] += 1

    # printGrid(grid)
    return [count for row in grid for count in row if count > 1]

allCounts = getGridCounts(generateLines(f))
print(len(allCounts))

f.seek(0)

allCountsWithDiagonals = getGridCounts(generateLines(f, True))
print(len(allCountsWithDiagonals))

