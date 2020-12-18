import file_input
n = file_input.get_numerical_input(1)

for i in range(len(n)):
    for j in range(i):
        if n[i] + n[j] == 2020:
            print(n[i] * n[j])

for i in range(len(n)):
    for j in range(i):
        for k in range(j):
            if n[i] + n[j] + n[k] == 2020:
                print(n[i] * n[j] * n[k])
