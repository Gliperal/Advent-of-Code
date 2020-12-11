import file_input
seats = [line.strip() for line in file_input.get_input(11)]
width = len(seats[0])
height = len(seats)

ADJACENT = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
)

def p1_neighbors(seats, y, x):
    n = 0
    for adj in ADJACENT:
        n_x = x + adj[0]
        n_y = y + adj[1]
        if (n_x >= 0 and n_x < width and
            n_y >= 0 and n_y < height and
            seats[n_y][n_x] == '#'):
            n += 1
    return n

def p2_neighbors(seats, y, x):
    n = 0
    for adj in ADJACENT:
        n_x = x + adj[0]
        n_y = y + adj[1]
        while (n_x >= 0 and n_x < width and
            n_y >= 0 and n_y < height):
            if seats[n_y][n_x] == '#':
                n += 1
                break
            elif seats[n_y][n_x] == 'L':
                break
            n_x += adj[0]
            n_y += adj[1]
    return n

def step(seats, neighbors, death):
    print('step')
    altered = False
    new_seats = []
    for y in range(height):
        new_row = []
        for x in range(width):
            n = neighbors(seats, y, x)
            if seats[y][x] == 'L' and n == 0:
                new_row.append('#')
                altered = True
            elif seats[y][x] == '#' and n >= death:
                new_row.append('L')
                altered = True
            else:
                new_row.append(seats[y][x])
        new_seats.append(new_row)
    if altered:
        return new_seats
    else:
        return None

while True:
    #new_seats = step(seats, p1_neighbors, 4)
    new_seats = step(seats, p2_neighbors, 5)
    if new_seats == None:
        print(''.join([''.join(row) for row in seats]).count('#'))
        break
    else:
        seats = new_seats
