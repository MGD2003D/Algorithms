import heapq

def sync_heaps(active_heap, remove_heap):
    while remove_heap and active_heap[0] == remove_heap[0]:
        heapq.heappop(active_heap)
        heapq.heappop(remove_heap)

@profile
def process_commands(commands):
    active_heap = []
    remove_heap = []
    results = []

    for command in commands:
        action, k = command.split()
        k = int(k)

        if action == '+1':
            heapq.heappush(active_heap, -k)
        elif action == '-1':
            heapq.heappush(remove_heap, -k)
        elif action == '0':
            sync_heaps(active_heap, remove_heap)
            temp = []

            for _ in range(k-1):
                temp.append(heapq.heappop(active_heap))
                sync_heaps(active_heap, remove_heap)

            results.append(str(-active_heap[0]))

            for item in temp:
                heapq.heappush(active_heap, item)

    return results

with open('resources/input.txt', 'r') as file:
    n = int(file.readline().strip())
    commands = [file.readline().strip() for _ in range(n)]

results = process_commands(commands)

with open('resources/output.txt', 'w') as file:
    file.write('\n'.join(results))
