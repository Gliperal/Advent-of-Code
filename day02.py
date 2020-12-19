import file_input
lines = file_input.get_input(2)

part1 = 0
part2 = 0
for line in lines:
    rules, password = line.split(':')
    # this leaves an extra leading space in the password...
    renge, letter = rules.split(' ')
    low, high = [int(v) for v in renge.split('-')]
    if password.count(letter) in range(low, high+1):
        part1 += 1
    count = 0
    # ...but they're 1-indexed so it balances out
    if password[low] == letter:
        count += 1
    if password[high] == letter:
        count += 1
    if count == 1:
        part2 += 1
print(part1)
print(part2)
