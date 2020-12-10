def get_input(day):
    with open('input{:02d}.txt'.format(day), 'r') as file:
        lines = [line for line in file]
    return lines

def get_numerical_input(day):
    with open('input{:02d}.txt'.format(day), 'r') as file:
        lines = [int(line) for line in file]
    return lines
