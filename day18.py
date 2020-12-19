import file_input
lines = file_input.get_input(18)

def reduce_part1(expr):
    while True:
        if expr[0] == '(':
            expr = reduce(expr[1:])
        # assume the first term is a number at this point
        elif len(expr) == 1:
            return expr
        elif expr[1] == ')':
            expr.pop(1)
            return expr
        # the second term is an operator
        elif expr[2] == '(':
            expr = expr[:2] + reduce(expr[3:])
        # the third term is a number
        elif expr[1] == '+':
            expr = [expr[0] + expr[2]] + expr[3:]
        elif expr[1] == '*':
            expr = [expr[0] * expr[2]] + expr[3:]

def reduce(expr):
    # stupid dumb parenthesis
    while ')' in expr:
        right = expr.index(')')
        left = right-1
        while expr[left] != '(':
            left -= 1
        expr = expr[:left] + reduce(expr[left+1:right]) + expr[right+1:]
    while '+' in expr:
        op = expr.index('+')
        expr = expr[:op-1] + [expr[op-1] + expr[op+1]] + expr[op+2:]
    while '*' in expr:
        op = expr.index('*')
        expr = expr[:op-1] + [expr[op-1] * expr[op+1]] + expr[op+2:]
    return [expr[0]]

total = 0
for line in lines:
    # I hate input parsing
    expr = line.strip().replace('(', ' ( ').replace(')', ' ) ').split()
    for i in range(len(expr)):
        if expr[i].isnumeric():
            expr[i] = int(expr[i])
    total += reduce(expr)[0]
print(total)
