def read_segments_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        segments = [list(map(int, line.split())) for line in file]
    return segments

@profile
def find_min_points(segments):
    segments.sort(key=lambda x: x[1])
    points = []
    while segments:
        current_point = segments[0][1]
        points.append(current_point)
        segments = [s for s in segments if s[0] > current_point]
    return points

def write_points_to_file(filename, points):
    with open(filename, 'w') as file:
        file.write(f"{len(points)}\n")
        file.write(' '.join(map(str, points)))

segments = read_segments_from_file('resources/input.txt')
points = find_min_points(segments)
write_points_to_file('resources/output.txt', points)
