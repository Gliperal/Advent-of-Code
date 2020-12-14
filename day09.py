import file_input
lines = file_input.get_numerical_input(9)

def contains_sum(num, addends):
    for i in range(25):
        for j in range(i):
            if addends[i] + addends[j] == num:
                return True
    return False

def series_sum(num, series):
    total = 0
    i = 0
    while True:
        total += series[i]
        if total >= num:
            if total == num:
                return series[:i+1]
            return None
        i += 1

for i in range(25, len(lines)):
    if not contains_sum(lines[i], lines[i-25:i]):
        key = lines[i]
        print(key)

for i in range(len(lines)):
    series = series_sum(key, lines[i:])
    if series != None:
        series.sort()
        print(series[0] + series[-1])
        break
