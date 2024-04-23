import heapq

@profile
def process_operations(input_file, output_file):
    heap = []
    deleted_or_updated = set()
    current_value = {}
    operation_index = 0

    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        n = int(fin.readline())
        for _ in range(n):
            line = fin.readline().strip().split()
            operation = line[0]

            if operation == 'A':
                value = int(line[1])
                heapq.heappush(heap, (value, operation_index))
                current_value[operation_index] = value
                operation_index += 1

            elif operation == 'X':
                while heap:
                    min_val, idx = heapq.heappop(heap)
                    if idx not in deleted_or_updated:
                        fout.write(f"{min_val}\n")
                        deleted_or_updated.add(idx)
                        break
                else:
                    fout.write("*\n")

            elif operation == 'D':
                idx_to_update = int(line[1]) - 1
                new_val = int(line[2])
                if idx_to_update in current_value:
                    deleted_or_updated.add(idx_to_update)
                    current_value[operation_index] = new_val
                    heapq.heappush(heap, (new_val, operation_index))
                    operation_index += 1

        while len(deleted_or_updated) < operation_index:
            _, idx = heapq.heappop(heap)
            if idx not in deleted_or_updated:
                fout.write(f"{current_value[idx]}\n")
                deleted_or_updated.add(idx)
            if not heap:
                break

        for _ in range(operation_index - len(deleted_or_updated)):
            fout.write("*\n")

process_operations('resources/input.txt', 'resources/output.txt')