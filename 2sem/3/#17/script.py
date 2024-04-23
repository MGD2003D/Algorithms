
def min_k_connected(input_file, output_file):
    with open(input_file, 'r') as file:
        n, m = map(int, file.readline().split())
        roads = [list(map(int, file.readline().split())) for _ in range(m)]

    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v in roads:
        dist[u - 1][v - 1] = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] == inf and i != j:
                dist[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    max_k = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] > max_k:
                max_k = dist[i][j]

    with open(output_file, 'w') as file:
        file.write(str(max_k))

min_k_connected('resources/input.txt', 'resources/output.txt')
