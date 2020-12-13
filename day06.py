import file_input
lines = file_input.get_input(6)
groups = ''.join(lines).split('\n\n')

# Part 1
total = 0
for group in groups:
    answered = [False] * 26
    for answer in group:
        if answer >= 'a' and answer <= 'z':
            answered[ord(answer)-ord('a')] = True
    total += answered.count(True)
print(total)

# Part 2
total = 0
for group in groups:
    answered = [True] * 26
    for person in group.split('\n'):
        if person.strip() == '': # empty line
            continue
        for i in range(26):
            if chr(ord('a') + i) not in person:
                answered[i] = False
    total += answered.count(True)
print(total)
