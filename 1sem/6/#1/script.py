@profile
def process_operations(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    elements_set = set()

    with open(output_file, 'w') as f:
        for line in lines[1:]:
            operation, value = line.split()
            value = int(value)

            if operation == 'A':
                elements_set.add(value)
            elif operation == 'D':
                elements_set.discard(value)
            elif operation == '?':
                f.write('Y\n' if value in elements_set else 'N\n')


process_operations('resources/input.txt', 'resources/output.txt')
