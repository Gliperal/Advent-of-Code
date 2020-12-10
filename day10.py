adapters = []
with open('input10.txt') as file:
    adapters = [int(line) for line in file]
adapters.sort()

def part1():
    three = 1 # at the end
    one = 1 # at the start
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if diff == 3:
            three += 1
        elif diff == 1:
            one += 1
    print(one)
    print(three)
    print(one * three)

def bridge(v):
    """
    The number of ways to bridge a voltage difference of v
    """
    if v < 0:
        return 0
    if v == 0:
        return 1
    if v == 1:
        return 1
    return bridge(v-1) + bridge(v-2) + bridge(v-3)

def part2():
    # we no longer care about 3-voltage gaps; those are mandatory
    adapters.insert(0, 0) # add the outlet
    chains = [] # lengths of 1-voltage chains in # of jumps
    current_chain = 0
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if diff == 1:
            current_chain += 1
        elif diff == 3 and current_chain > 0:
            chains.append(current_chain)
            current_chain = 0
    if current_chain > 0:
        chains.append(current_chain)
    combinations = 1
    for length in chains:
        combinations *= bridge(length)
    print(combinations)


# part1()
part2()
