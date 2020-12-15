import math
import file_input
lines = file_input.get_input(12)

# Using Cartesian coordinates, not screen coordinates

def sin(angle):
    return math.sin(angle * math.pi / 180)

def cos(angle):
    return math.cos(angle * math.pi / 180)

def rotate(coords, angle):
    return [
        coords[0] * cos(angle) - coords[1] * sin(angle),
        coords[0] * sin(angle) + coords[1] * cos(angle)
    ]

def part1():
    x = 0
    y = 0
    direction = [1, 0]
    for line in lines:
        order = line[0]
        num = int(line[1:])
        if order == 'N':
            y += num
        elif order == 'S':
            y -= num
        elif order == 'E':
            x += num
        elif order == 'W':
            x -= num
        elif order == 'L':
            direction = rotate(direction, num)
        elif order == 'R':
            direction = rotate(direction, 0 - num)
        elif order == 'F':
            x += direction[0] * num
            y += direction[1] * num
    print(abs(x) + abs(y))

def part2():
    x = 0
    y = 0
    waypoint = [10, 1]
    for line in lines:
        order = line[0]
        num = int(line[1:])
        if order == 'N':
            waypoint[1] += num
        elif order == 'S':
            waypoint[1] -= num
        elif order == 'E':
            waypoint[0] += num
        elif order == 'W':
            waypoint[0] -= num
        elif order == 'L':
            waypoint = rotate(waypoint, num)
        elif order == 'R':
            waypoint = rotate(waypoint, 0 - num)
        elif order == 'F':
            x += waypoint[0] * num
            y += waypoint[1] * num
    print(abs(x) + abs(y))

part1()
part2()
