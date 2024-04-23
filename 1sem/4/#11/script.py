@profile
def process_queue(input_file, output_file):
    with open(input_file, 'r') as f:
        n, m = map(int, f.readline().split())
        queue = list(map(int, f.readline().split()))

    current_pos = 0
    while m > 0 and current_pos < len(queue):
        if queue[current_pos] <= m:
            m -= queue[current_pos]
            queue[current_pos] = 0
        else:
            queue[current_pos] -= m
            m = 0
        current_pos += 1

    queue = [x for x in queue if x > 0]

    with open(output_file, 'w') as f:
        if len(queue) == 0:
            f.write("-1\n")
        else:
            f.write(f"{len(queue)}\n")
            f.write(' '.join(map(str, queue)) + '\n')


process_queue('resources/input.txt', 'resources/output.txt')

