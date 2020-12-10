import re
import file_input
lines = file_input.get_input(4)
raw_passports = ''.join(lines).split('\n\n')
passports = [
    dict([pair.split(':') for pair in raw.split()])
    for raw in raw_passports
]

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def semivalid(passport):
    for field in FIELDS:
        if field not in passport:
            return False
    return True

HAIR_PATTERN = re.compile(r'^#(\d|[a-f]){6}$')
ID_PATTERN = re.compile(r'^\d{9}$')
EYES = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_height(height):
    try:
        if height.endswith('cm'):
            h = int(height[:-2])
            return h >= 150 and h <= 193
        elif height.endswith('in'):
            h = int(height[:-2])
            return h >= 59 and h <= 76
        else:
            return False
    except ValueError:
        return False

def valid(passport):
    try:
        return (
            passport['byr'] >= 1920 and passport['byr'] <= 2002 and
            passport['iyr'] >= 2010 and passport['iyr'] <= 2020 and
            passport['eyr'] >= 2020 and passport['eyr'] <= 2030 and
            valid_height(passport['hgt']) and
            HAIR_PATTERN.match(passport['hcl']) != None and
            passport['ecl'] in EYES and
            ID_PATTERN.match(passport['pid'])
        )
    except KeyError:
        return False

# part 1
print(len([p for p in passports if semivalid(p)]))
# part 2
for passport in passports:
    try:
        passport['byr'] = int(passport['byr'])
        passport['iyr'] = int(passport['iyr'])
        passport['eyr'] = int(passport['eyr'])
    except KeyError:
        pass
print(len([p for p in passports if valid(p)]))
