def read_graph(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().strip().split())
        edges = []
        for _ in range(m):
            u, v, w = map(int, file.readline().strip().split())
            edges.append((u, v, w))
        start_vertex = int(file.readline().strip())
    return n, edges, start_vertex

def write_result(file_path, distances):
    with open(file_path, 'w') as file:
        for dist in distances:
            file.write(f"{dist}\n")

@profile
def bellman_ford(n, edges, start_vertex):
    distance = [float('inf')] * (n + 1)
    distance[start_vertex] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for _ in range(n):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = float('-inf')

    result = []
    for dist in distance[1:]:
        if dist == float('inf'):
            result.append('*')
        elif dist == float('-inf'):
            result.append('-')
        else:
            result.append(str(dist))
    return result

input_path = "resources/input.txt"
output_path = "resources/output.txt"

n, edges, start_vertex = read_graph(input_path)
distances = bellman_ford(n, edges, start_vertex)
write_result(output_path, distances)