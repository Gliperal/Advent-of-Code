import file_input
starting_cups = [int(c) for c in list(file_input.get_input(23)[0])]

cups = starting_cups.copy()
for move in range(100):
    pickup = cups[1:4]
    cups.pop(1)
    cups.pop(1)
    cups.pop(1)
    destination = -1
    destination_value = cups[0] - 1
    while destination == -1:
        if destination_value <= 0:
            destination_value = 9
        try:
            destination = cups.index(destination_value)
        except ValueError:
            destination_value -= 1
            continue
    cups = cups[:destination+1] + pickup + cups[destination+1:]
    cups = cups[1:] + cups[:1] # rotate cups

print(cups)


# Part 2

# Building the cups
cups = [None] # 0th element = placeholder
for i in range(1, 1000001):
    cups.append({'value': i})
for i in range(10, 1000000):
    cups[i]['next'] = cups[i + 1]
cups[1000000]['next'] = cups[starting_cups[0]]
for i in range(1, 10):
    try:
        cups[i]['next'] = cups[starting_cups[starting_cups.index(i) + 1]]
    except IndexError:
        cups[i]['next'] = cups[10]

for cup in cups[1:15] + cups[999998:]:
    print('Cup {:d} (next cup {:d})'.format(cup['value'], cup['next']['value']))

# Playing the game
current = cups[starting_cups[0]]
for move in range(10000000):
    pickup = current['next']
    pickup_values = [
        pickup['value'],
        pickup['next']['value'],
        pickup['next']['next']['value']
    ]
    current['next'] = current['next']['next']['next']['next']
    destination_value = current['value']
    while True:
        destination_value -= 1
        if destination_value <= 0:
            destination_value = 1000000
        if destination_value not in pickup_values:
            break
    destination = cups[destination_value]
    pickup['next']['next']['next'] = destination['next']
    destination['next'] = pickup
    current = current['next']

print(cups[1]['next']['value'] * cups[1]['next']['next']['value'])
