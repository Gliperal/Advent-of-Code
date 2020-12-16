import file_input
lines = file_input.get_input(16)

s = ''.join(lines).split('\n\n')
fields_raw = s[0].split('\n')
my_ticket = s[1].split('\n')[1]
tickets_raw = s[2].split('\n')[1:-1] # last line is empty

fields = dict()
for field in fields_raw:
    name, desc = field.split(':')
    ranges = []
    for ranges_raw in desc.split('or'):
        low, high = [int(x.strip()) for x in ranges_raw.split('-')]
        ranges.append(range(low, high+1))
    fields[name] = ranges
tickets = [
    [int(field.strip()) for field in ticket.split(',')]
    for ticket in tickets_raw
]

def part1():
    ok_values = [False] * 1000
    for name in fields:
        for r in fields[name]:
            for i in r:
                ok_values[i] = True
    total = 0
    i = 0
    while i < len(tickets):
        ticket = tickets[i]
        bad_ticket = False
        for value in ticket:
            if not ok_values[value]:
                total += value
                bad_ticket = True
        if bad_ticket:
            tickets.pop(i)
        else:
            i += 1
    print(total)

def field_can_be(field, position):
    for ticket in tickets:
        value = ticket[position]
        if all(value not in renge for renge in field):
            return False
    return True

def part2():
    for name in fields:
        print(name + ' can be: ', end='')
        for position in range(len(fields)):
            if field_can_be(fields[name], position):
                print(str(position) + ' ', end='')
        print()
    print(my_ticket)
    # and then I just did it by hand c:

part1()
part2()
