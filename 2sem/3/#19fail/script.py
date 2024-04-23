import math

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    points = [tuple(map(int, line.split())) for line in lines[1:n+1]]
    k = int(lines[-1])
    return points, k

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_edges(points):
    edges = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i < j:
                edges.append((distance(p1, p2), i, j))
    return edges

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

def clustering(points, k):
    n = len(points)
    edges = create_edges(points)
    edges.sort(key=lambda x: -x[0])
    parent = list(range(n))
    rank = [0] * n
    num_clusters = n
    for edge in edges:
        d, x, y = edge
        xroot = find(parent, x)
        yroot = find(parent, y)
        if xroot != yroot:
            if num_clusters <= k:
                return d
            union(parent, rank, xroot, yroot)
            num_clusters -= 1

def write_output(filename, d):
    with open(filename, 'w') as file:
        file.write(f"{d:.7f}\n")

points, k = read_input('resources/input.txt')
d = clustering(points, k)
write_output('resources/output.txt', d)
