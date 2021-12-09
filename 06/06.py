f = open('06/input.txt', 'r')

fishAges = [int(char.strip()) for char in f.readlines()[0].split(',')]

# Naive idea that is easy to follow but slooooow 🐌

for day in range(1, 81):
    spawnedChildren = []

    # Remember how many zeroes we had **before** changing the list.
    newFishCount = fishAges.count(0)

    # Zeroes become sixes, the rest gets decreased by one.
    fishAges = [6 if age == 0 else age - 1 for age in fishAges]

    # Create new fish
    fishAges.extend([8] * newFishCount)

    print('after ' + str(day) + ' day(s): ' + str(len(fishAges)))


# Reset
f.seek(0)
fishAges = [int(char.strip()) for char in f.readlines()[0].split(',')]


# Much short & more performant solution (but harder to get right 😅)

# Indices represent age and values represent how often this age occurs in the swarm.
ages = [0] * 9

for fish in fishAges:
    ages[fish] += 1


for day in range(1, 257):
    (ages[0],ages[1],ages[2],ages[3],ages[4],ages[5],ages[6],ages[7],ages[8]) = (ages[1],ages[2],ages[3],ages[4],ages[5],ages[6],ages[0] + ages[7],ages[8], ages[0])

    print('after ' + str(day) + ' day(s): ' + str(sum(ages)))
