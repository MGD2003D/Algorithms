def read_input(file_path):
    with open(file_path, 'r') as file:
        points = [tuple(map(int, line.strip().split())) for line in file.readlines()[1:]]
    return points


def write_output(file_path, length):
    with open(file_path, 'w') as file:
        file.write(f"{length:.9f}")


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


@profile
def kruskal(points):
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            edges.append((distance(points[i], points[j]), i, j))
    edges.sort(key=lambda x: x[0])

    parent = [i for i in range(len(points))]
    rank = [0] * len(points)

    min_length = 0
    for edge in edges:
        w, u, v = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            min_length += w

    return min_length


input_file = "resources/input.txt"
output_file = "resources/output.txt"

points = read_input(input_file)
min_length = kruskal(points)
write_output(output_file, min_length)