def digital_sort(n, m, k, columns):
    indices = list(range(n))

    for phase in range(k):
        current_column = m - 1 - phase

        indices.sort(key=lambda x: columns[current_column][x])

    return [index + 1 for index in indices]

@profile
def main():
    with open('resources/input.txt', 'r') as file:
        n, m, k = map(int, file.readline().split())
        columns = [list(file.readline().strip()) for _ in range(m)]

    sorted_indices = digital_sort(n, m, k, columns)

    with open('resources/output.txt', 'w') as file:
        file.write(' '.join(map(str, sorted_indices)))


main()

