import file_input
lines = file_input.get_input(8)

def part1():
    visited = set()
    ip = 0
    eax = 0
    while True:
        if ip in visited:
            print(eax)
            break
        visited.add(ip)
        line = lines[ip]
        instr = line[:3]
        arg = int(line[4:])
        if instr == 'acc':
            eax += arg
            ip += 1
        elif instr == 'jmp':
            ip += arg
        else:
            ip += 1

def run_program(visited, altered, ip, eax):
    if ip == len(lines):
        print(eax)
        return True
    if visited[ip]:
        return False
    visited[ip] = True
    line = lines[ip]
    instr = line[:3]
    arg = int(line[4:])
    if instr == 'acc':
        run_program(visited, altered, ip + 1, eax + arg)
    elif instr == 'jmp':
        run_program(visited, altered, ip + arg, eax)
        if not altered:
            run_program(visited, True, ip + 1, eax)
    else:
        run_program(visited, altered, ip + 1, eax)
        if not altered:
            run_program(visited, True, ip + arg, eax)
    visited[ip] = False

def part2():
    visited = [False] * len(lines)
    run_program(visited, False, 0, 0)

#part1()
part2()
