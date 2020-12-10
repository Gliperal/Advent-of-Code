import file_input
lines = file_input.get_input(5)

# Part 1
seats = [line.replace('F', '0').replace('R', '1').replace('B', '1').replace('L', '0') for line in lines]
seats.sort()
print(int(seats[-1], 2))

# Part 2
prev = -1000
for seat in seats:
    num = int(seat, 2)
    if num - prev == 2:
        print(prev + 1)
    prev = num
