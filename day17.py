import file_input
lines = [line.strip() for line in file_input.get_input(17)]

input_height = len(lines)
input_width = len(lines[0])
cycles = 6

width = cycles * 2 + input_width
height = cycles * 2 + input_height
depth = 1 + cycles * 2

def display_grid(grid):
    for z in range(depth):
        print('z={:d}'.format(z))
        for y in range(height):
            for x in range(width):
                if grid[z][y][x]:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print()

# Making the base layer
base_layer = []
for y in range(cycles):
    base_layer.append([False] * width)
for y in range(input_height):
    row = [False] * cycles
    for x in range(input_width):
        row.append(lines[y][x] == '#')
    row += [False] * cycles
    base_layer.append(row)
for y in range(cycles):
    base_layer.append([False] * width)

def make_layer(w, h):
    layer = []
    for y in range(h):
        layer.append([False] * w)
    return layer

# Making the rest of the 3D grid
grid = []
for z in range(cycles):
    grid.append(make_layer(width, height))
grid.append(base_layer)
for z in range(cycles):
    grid.append(make_layer(width, height))

def count_neighbors(grid, x, y, z):
    count = 0
    for xi in [-1, 0, 1]:
        for yi in [-1, 0, 1]:
            for zi in [-1, 0, 1]:
                try:
                    if ((xi != 0 or yi != 0 or zi != 0) and
                        grid[z + zi][y + yi][x + xi]):
                        count += 1
                except IndexError:
                    pass
    return count

def step(grid):
    new_grid = [make_layer(width, height) for z in range(depth)]
    total = 0
    for z in range(depth):
        for y in range(height):
            for x in range(width):
                neighbors = count_neighbors(grid, x, y, z)
                if grid[z][y][x]:
                    new_grid[z][y][x] = (neighbors >= 2 and neighbors <= 3)
                else:
                    new_grid[z][y][x] = (neighbors == 3)
    return new_grid

for c in range(cycles):
    grid = step(grid)

count = 0
for z in range(depth):
    for y in range(height):
        for x in range(width):
            if grid[z][y][x]:
                count += 1
print(count)




#########################################

# New idea, we're using a dict

grid = dict()

for y in range(input_height):
    for x in range(input_width):
        if lines[y][x] == '#':
            grid[(x, y, 0, 0)] = True

def count_neighbors_redux(grid, x, y, z, w):
    count = 0
    for xi in [-1, 0, 1]:
        for yi in [-1, 0, 1]:
            for zi in [-1, 0, 1]:
                for wi in [-1, 0, 1]:
                    try:
                        if ((xi != 0 or yi != 0 or zi != 0 or wi != 0) and
                            grid[(x + xi, y + yi, z + zi, w + wi)]):
                            count += 1
                    except KeyError:
                        pass
    return count

def step_redux(grid):
    new_grid = dict()
    total = 0
    for w in range(0-cycles, cycles+1):
        for z in range(0-cycles, cycles+1):
            for y in range(0-cycles, cycles+height+1):
                for x in range(0-cycles, cycles+width+1):
                    neighbors = count_neighbors_redux(grid, x, y, z, w)
                    if (x, y, z, w) in grid and grid[(x, y, z, w)]:
                        new_grid[(x, y, z, w)] = (neighbors >= 2 and
                                                  neighbors <= 3)
                    else:
                        new_grid[(x, y, z, w)] = (neighbors == 3)
    return new_grid

for c in range(cycles):
    grid = step_redux(grid)

count = 0
for key in grid:
    if grid[key]:
        count += 1
print(count)

# This is so slow lmao but it works
