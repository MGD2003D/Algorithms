def read_input(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        procedures = {}
        for _ in range(n):
            proc_name = file.readline().strip()
            k = int(file.readline().strip())
            calls = [file.readline().strip() for _ in range(k)]
            procedures[proc_name] = calls
            file.readline()
    return procedures

def can_call_itself(procedures, start_proc, current_proc, visited=None):
    if visited is None:
        visited = set()
    if current_proc in visited:
        return False
    visited.add(current_proc)
    for called_proc in procedures[current_proc]:
        if called_proc == start_proc or can_call_itself(procedures, start_proc, called_proc, visited):
            return True
    return False

def write_output(file_name, results):
    with open(file_name, 'w') as file:
        for result in results:
            file.write(result + '\n')

@profile
def main(input_file, output_file):
    procedures = read_input(input_file)
    results = []
    for proc in procedures:
        if can_call_itself(procedures, proc, proc):
            results.append('YES')
        else:
            results.append('NO')
    write_output(output_file, results)

main('resources/input.txt', 'resources/output.txt')