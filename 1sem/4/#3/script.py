def is_valid_sequence(s):
    stack = []
    pairs = {')': '(', ']': '['}

    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if not stack else 'NO'

@profile
def process_sequences(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    results = [is_valid_sequence(lines[i].strip()) for i in range(1, n + 1)]

    with open(output_file, 'w') as f:
        for result in results:
            f.write(result + '\n')



process_sequences('resources/input.txt', 'resources/output.txt')
