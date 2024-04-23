@profile
def find_mismatch_positions(k, t, p):
    len_t, len_p = len(t), len(p)
    results = []
    for start in range(len_t - len_p + 1):
        mismatch_count = 0
        for j in range(len_p):
            if t[start + j] != p[j]:
                mismatch_count += 1
                if mismatch_count > k:
                    break
        if mismatch_count <= k:
            results.append(start)
    return results


@profile
def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        data = file.readlines()

    with open(output_filename, 'w') as file:
        for line in data:
            k, t, p = line.split()
            k = int(k)
            matches = find_mismatch_positions(k, t, p)
            output = f"{len(matches)}" + (' ' + ' '.join(map(str, matches)) if matches else '')
            file.write(output + '\n')


process_file('resources/input.txt', 'resources/output.txt')