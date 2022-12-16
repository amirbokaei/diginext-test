def q3(arr: list):
    count = 0
    arr_enum = [*enumerate(arr)]
    arr_len = len(arr)

    arr_enum.sort(key=lambda x: x[1])

    visited = {k: False for k in range(arr_len)}

    for i in range(arr_len):
        cycle_size = 0
        j = i
        if visited[i] or arr_enum[i][0] == i:
            continue

        while not visited[j]:
            visited[j] = True

            j = arr_enum[j][0]
            cycle_size += 1

        if cycle_size > 0:
            count += cycle_size - 1

    return count


arr = [7, 1, 3, 2, 4, 5, 6]
print(q3(arr))
