import file_input
line = file_input.get_input(15)[0]
starting_numbers = [int(x) for x in line.split(',')]

last_spoken = [None] * 30000000

# Update last spoken for all the starting numbers but one
# (it will be updated on the first game round)
for i in range(len(starting_numbers) - 1):
    last_spoken[starting_numbers[i]] = i

previous = starting_numbers[-1]

for turn in range(len(starting_numbers), 30000000):
    # Find out when the previous number was last spoken
    if last_spoken[previous] == None:
        current = 0
    else:
        current = turn - 1 - last_spoken[previous]
    # Update last spoken for the previous number
    last_spoken[previous] = turn - 1
    # Set current number to previous as we ready the next turn
    previous = current
    if (turn == 30000000 - 1):
        print(current)
