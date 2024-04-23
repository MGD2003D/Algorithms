class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.max_stack[-1]:
                self.max_stack.pop()
            return val

    def max(self):
        return self.max_stack[-1] if self.max_stack else None

@profile
def process_commands(input_file, output_file):
    max_stack = MaxStack()

    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        results = []

        for _ in range(n):
            command = f.readline().strip().split()
            if command[0] == "push":
                max_stack.push(int(command[1]))
            elif command[0] == "pop":
                max_stack.pop()
            elif command[0] == "max":
                results.append(str(max_stack.max()))

    with open(output_file, 'w') as f:
        f.write('\n'.join(results))

process_commands('resources/input.txt', 'resources/output.txt')
