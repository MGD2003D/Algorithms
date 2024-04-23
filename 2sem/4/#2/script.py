@profile
def calculate_x(message):
    message = message.replace(" ", "")
    n = len(message)
    if n < 3:
        return 0

    from collections import defaultdict
    positions = defaultdict(list)
    for i, char in enumerate(message):
        positions[char].append(i)

    x = 0
    for letter, pos_list in positions.items():
        for i in range(len(pos_list)):
            for j in range(i + 1, len(pos_list)):
                if pos_list[j] - pos_list[i] > 1:
                    x += (pos_list[j] - pos_list[i] - 1)

    return x


@profile
def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        input_string = file.read().strip()

    x = calculate_x(input_string)

    with open(output_filename, 'w') as file:
        file.write(str(x))



process_file('resources/input.txt', 'resources/output.txt')