@profile
def simulate_hash_table_operations(input_file, output_file):
    with open(input_file, 'r') as f:
        N, X, A, B = map(int, f.readline().split())
        AC, BC, AD, BD = map(int, f.readline().split())
    hash_table = set()
    for _ in range(N):
        if X in hash_table:
            A = (A + AC) % 10**3
            B = (B + BC) % 10**15
        else:
            hash_table.add(X)
            A = (A + AD) % 10**3
            B = (B + BD) % 10**15
        X = (X * A + B) % 10**15
    with open(output_file, 'w') as f:
        f.write(f"{X} {A} {B}")

input_file = 'resources/input.txt'
output_file = 'resources/output.txt'
simulate_hash_table_operations(input_file, output_file)
