data = [5, 6, 0, 1, 2, 4, 3, 9, 8, 7]

for j in range(0, 10):
    check_for_swap = False
    for i in range(0, 9):
        if data[i] > data[i + 1]:
            swap = data[i]
            data[i] = data[i + 1]
            data[i + 1] = swap
            check_for_swap = True
    if check_for_swap = False:
        break
print(j, data)
