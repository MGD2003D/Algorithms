def read_input(input_filename):
    with open(input_filename, 'r') as file:
        n = int(file.readline().strip())
        matrices = [list(map(int, file.readline().split())) for _ in range(n)]
        dims = [matrices[0][0]] + [matrices[i][1] for i in range(n)]
    return dims


def matrix_chain_order(dims):
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    s = [[None] * n for _ in range(n)]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k
    return s


def construct_optimal_order(s, i, j):
    if i == j:
        return 'A'
    else:
        return '(' + construct_optimal_order(s, i, s[i][j]) + construct_optimal_order(s, s[i][j] + 1, j) + ')'


# @profile
def solve(input_filename, output_filename):
    dims = read_input(input_filename)
    s = matrix_chain_order(dims)
    optimal_order = construct_optimal_order(s, 0, len(dims) - 2)
    with open(output_filename, 'w') as file:
        file.write(optimal_order)


solve('resources/input.txt', 'resources/output.txt')