@profile
def process_stack_commands(input_file, output_file):
    stack = []

    with open(input_file, 'r') as f:
        commands_count = int(f.readline().strip())
        for _ in range(commands_count):
            command = f.readline().strip()
            if command.startswith('+'):
                _, number = command.split()
                stack.append(int(number))
            elif command == '-':
                if stack:
                    removed_item = stack.pop()
                    with open(output_file, 'a') as output:
                        output.write(f'{removed_item}\n')


process_stack_commands('resources/input.txt', 'resources/output.txt')
