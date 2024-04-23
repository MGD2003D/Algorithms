M = 1000000001

class IntSet:
    def __init__(self):
        self.s = set()

    def add(self, i):
        self.s.add(i)

    def delete(self, i):
        self.s.discard(i)

    def find(self, i):
        return "Found" if i in self.s else "Not found"

    def sum(self, l, r):
        return sum(v for v in self.s if l <= v <= r)

@profile
def process_operations(input_file, output_file):
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        operations = [f.readline().strip() for _ in range(n)]

    result = []
    int_set = IntSet()
    last_sum = 0

    for op in operations:
        if op[0] == '+':
            int_set.add((int(op[1:]) + last_sum) % M)
        elif op[0] == '-':
            int_set.delete((int(op[1:]) + last_sum) % M)
        elif op[0] == '?':
            result.append(int_set.find((int(op[1:]) + last_sum) % M))
        elif op[0] == 's':
            l, r = map(int, op[1:].split())
            last_sum = int_set.sum((l + last_sum) % M, (r + last_sum) % M)
            result.append(last_sum)

    with open(output_file, 'w') as f:
        for line in result:
            f.write(f"{line}\n")

process_operations("resources/input.txt", "resources/output.txt")