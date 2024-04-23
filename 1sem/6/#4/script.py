from collections import OrderedDict

@profile
def process_commands(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    commands = lines[1:]
    ordered_map = OrderedDict()

    outputs = []
    for command in commands:
        parts = command.strip().split()
        operation = parts[0]

        if operation == "put":
            key, value = parts[1], parts[2]
            if key in ordered_map:
                ordered_map.move_to_end(key)
            ordered_map[key] = value

        elif operation == "delete":
            key = parts[1]
            if key in ordered_map:
                del ordered_map[key]

        elif operation == "get":
            key = parts[1]
            value = ordered_map.get(key, "<none>")
            outputs.append(value)

        elif operation == "prev":
            key = parts[1]
            keys = list(ordered_map.keys())
            if key in ordered_map and keys.index(key) > 0:
                prev_key = keys[keys.index(key) - 1]
                outputs.append(ordered_map[prev_key])
            else:
                outputs.append("<none>")

        elif operation == "next":
            key = parts[1]
            keys = list(ordered_map.keys())
            if key in ordered_map and keys.index(key) < len(keys) - 1:
                next_key = keys[keys.index(key) + 1]
                outputs.append(ordered_map[next_key])
            else:
                outputs.append("<none>")

    with open(output_file, 'w') as f:
        for output in outputs:
            f.write(f"{output}\n")

process_commands('resources/input.txt', 'resources/output.txt')
