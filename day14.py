import file_input
lines = file_input.get_input(14)

def create_mask(string):
    return [
        int(string.replace('X', '1'), 2),
        int(string.replace('X', '0'), 2)
    ]

def apply_mask(num, mask):
    return (num & mask[0]) | mask[1]

def part1():
    memory = dict()
    for line in lines:
        if line.startswith("mask = "):
            mask = create_mask(line[7:].strip())
        elif line.startswith("mem["):
            s = line[4:].split(']')
            addr = int(s[0])
            value = int(s[1][3:])
            memory[addr] = apply_mask(value, mask)
    total = 0
    for addr in memory:
        total += memory[addr]
    print(total)

def string_mask(addr, mask):
    addr = format(addr, 'b') # convert address to binary string
    if len(addr) < len(mask): # zero pad
        addr = '0' * (len(mask) - len(addr)) + addr
    addr = list(addr) # make that string mutable
    for i in range(len(mask)):
        if mask[0-i] != '0':
            addr[0-i] = mask[0-i]
    return ''.join(addr)

def write_memory(memory, addr, value):
    x = addr.find('X')
    if x == -1:
        memory[''.join(addr)] = value
    else:
        write_memory(memory, addr[:x] + '0' + addr[x+1:], value)
        write_memory(memory, addr[:x] + '1' + addr[x+1:], value)

def part2():
    memory = dict()
    for line in lines:
        if line.startswith("mask = "):
            mask = line[7:].strip()
        elif line.startswith("mem["):
            s = line[4:].split(']')
            addr = string_mask(int(s[0]), mask)
            value = int(s[1][3:])
            write_memory(memory, addr, value)
    total = 0
    for addr in memory:
        total += memory[addr]
    print(total)

#part1()
part2()
